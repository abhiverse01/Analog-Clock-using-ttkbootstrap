/*
------------------------------------------------------------------------------ 
This code was generated by Amplication. 
 
Changes to this file will be lost if the code is regenerated. 

There are other ways to to customize your code, see this doc to learn more
https://docs.amplication.com/how-to/custom-code

------------------------------------------------------------------------------
  */
import { PrismaService } from "../../prisma/prisma.service";
import { Prisma, Project as PrismaProject } from "@prisma/client";
import { LocalStorageService } from "src/storage/providers/local/local.storage.service";
import { InputJsonValue } from "src/types";
import { FileDownload, FileUpload } from "src/storage/base/storage.types";
import { LocalStorageFile } from "src/storage/providers/local/local.storage.types";

export class ProjectServiceBase {
  constructor(
    protected readonly prisma: PrismaService,
    protected readonly localStorageService: LocalStorageService
  ) {}

  async count(args: Omit<Prisma.ProjectCountArgs, "select">): Promise<number> {
    return this.prisma.project.count(args);
  }

  async projects(args: Prisma.ProjectFindManyArgs): Promise<PrismaProject[]> {
    return this.prisma.project.findMany(args);
  }
  async project(
    args: Prisma.ProjectFindUniqueArgs
  ): Promise<PrismaProject | null> {
    return this.prisma.project.findUnique(args);
  }
  async createProject(args: Prisma.ProjectCreateArgs): Promise<PrismaProject> {
    return this.prisma.project.create(args);
  }
  async updateProject(args: Prisma.ProjectUpdateArgs): Promise<PrismaProject> {
    return this.prisma.project.update(args);
  }
  async deleteProject(args: Prisma.ProjectDeleteArgs): Promise<PrismaProject> {
    return this.prisma.project.delete(args);
  }

  async uploadFiles<T extends Prisma.ProjectFindUniqueArgs>(
    args: Prisma.SelectSubset<T, Prisma.ProjectFindUniqueArgs>,
    file: FileUpload
  ): Promise<PrismaProject> {
    file.filename = `profilePicture-${args.where.id}.${file.filename
      .split(".")
      .pop()}`;
    const containerPath = "files";
    const files = await this.localStorageService.uploadFile(
      file,
      [],
      1000000,
      containerPath
    );

    return await this.prisma.project.update({
      where: args.where,

      data: {
        files: files as InputJsonValue,
      },
    });
  }

  async downloadFiles<T extends Prisma.ProjectFindUniqueArgs>(
    args: Prisma.SelectSubset<T, Prisma.ProjectFindUniqueArgs>
  ): Promise<FileDownload> {
    const { files } = await this.prisma.project.findUniqueOrThrow({
      where: args.where,
    });

    return await this.localStorageService.downloadFile(
      files as unknown as LocalStorageFile
    );
  }

  async deleteFiles<T extends Prisma.ProjectFindUniqueArgs>(
    args: Prisma.SelectSubset<T, Prisma.ProjectFindUniqueArgs>
  ): Promise<PrismaProject> {
    const { files } = await this.prisma.project.findUniqueOrThrow({
      where: args.where,
    });

    await this.localStorageService.deleteFile(
      files as unknown as LocalStorageFile
    );

    return await this.prisma.project.update({
      where: args.where,

      data: {
        files: Prisma.DbNull,
      },
    });
  }
}

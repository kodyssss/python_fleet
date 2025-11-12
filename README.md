# python_fleet DevSecOps 项目 README

## 项目概述
本项目是一个结合 **Fleet 设备管理**、**GitLab CI 自动化流水线**与 **NEU 安全扫描**的 DevSecOps 实践项目，旨在通过自动化流程实现代码开发、安全检测与设备管理的一体化，提升软件交付的安全性与效率。


## 技术栈
- **版本控制与 CI/CD**：GitLab
- **设备管理**：Fleet
- **安全扫描**：NEU 扫描工具
- **应用开发**：Python
- **容器化**：Docker


## 项目结构
```
python_fleet/
├── kustomize/          # Kustomize 配置目录（用于 Kubernetes 资源定制）
├── static/             # 静态资源目录
├── templates/          # 模板文件目录（如 Kubernetes 资源模板）
├── .gitlab-ci.yml      # GitLab CI 流水线配置文件
├── demo_web.py         # Python 示例 Web 应用
├── dockerfile          # Docker 镜像构建文件
├── scan.yaml           # NEU 安全扫描配置文件
└── README.md           # 本说明文件
```


## 功能说明
1. **GitLab CI 自动化流水线**
   通过 `.gitlab-ci.yml` 定义自动化流程，包含**代码编译、NEU 安全扫描、Docker 镜像构建、Fleet 设备同步**等环节，实现从代码提交到安全交付的全自动化。

2. **NEU 安全扫描**
   基于 `scan.yaml` 配置，对代码、依赖、容器镜像等进行**漏洞检测、合规性检查**，确保代码安全性。

3. **Fleet 设备管理集成**
   实现与 Fleet 平台的对接，支持**设备状态监控、配置下发、安全策略同步**，保障终端设备的合规性。

4. **Python 示例应用**
   `demo_web.py` 提供简单 Web 服务示例，展示应用开发与容器化部署流程。


## 快速开始

### 前提条件
- 拥有 GitLab 项目仓库权限
- 已部署 Fleet 平台并配置访问凭证
- 已接入 NEU 扫描服务


### 步骤 1：克隆项目
```bash
git clone <项目Git地址>
cd python_fleet
```

### 步骤 2：配置 GitLab CI
修改 `.gitlab-ci.yml` 中的**环境变量、服务地址**（如 Fleet 地址、NEU 扫描服务地址），适配你的环境。

### 步骤 3：触发 CI 流水线
提交代码至 GitLab 仓库，自动触发 CI 流水线：
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 步骤 4：查看流水线与扫描结果
在 GitLab 项目的 **CI/CD -> 流水线** 中查看执行过程，在 **作业日志** 中查看 NEU 扫描报告与 Fleet 同步状态。


## 贡献指南
欢迎通过以下方式参与项目：
- 提交 Issue 反馈 bug 或提出功能建议
- 提交 Pull Request 贡献代码（请遵循代码规范与提交说明）


## 联系与支持
若有任何疑问，可通过以下方式联系：
- 邮件：[你的邮箱]
- GitLab 项目 Issue 板块


---

通过本项目，你可以快速实践 DevSecOps 理念，将安全左移融入开发流程，同时结合设备管理实现端到端的合规性保障。

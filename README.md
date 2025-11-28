# python_fleet

一个基于 **GitLab CI + Fleet 设备管理 + NEU 安全扫描 + Python Web 应用** 的 DevSecOps Demo 项目。

本项目演示如何在企业环境中，通过自动化流水线实现 **代码开发 → 安全扫描 → 构建镜像 → Fleet 设备配置同步** 的 DevSecOps 全流程。

---

## 📌 项目概述

`python_fleet` 是一个面向企业内部安全与终端管理场景设计的 Demo 项目。
通过 GitLab CI/CD、NEU 安全扫描服务和 Fleet 设备管理平台，构建了一个安全高效的 DevSecOps 流程。

该项目包含：

* Python 示例 Web 服务
* Docker 镜像构建流程
* 自动化安全扫描（NEU）
* 与 Fleet 的对接（配置下发 / 设备同步）
* 完整 GitLab CI 配置
* Kubernetes 部署示例（由 Kustomize 模板管理）

---

## 🏗️ 整体架构（DevSecOps 流程）

```
开发者提交代码 ───────────────┐
                               ▼
                      GitLab CI Pipeline
 ┌──────────────────────────────────────────────────────────┐
 │ 1. 代码检查 / Lint                                       │
 │ 2. NEU 代码依赖 / 容器扫描 (scan.yaml)                   │
 │ 3. 构建 Python Web Docker 镜像                          │
 │ 4. 推送镜像到 Registry（可选，无 Harbor 依赖）           │
 │ 5. 触发 Fleet 配置同步 / 应用交付                        │
 └──────────────────────────────────────────────────────────┘
                               ▼
                       Fleet 设备管理平台
                               ▼
                   设备拉取配置 → 部署安全策略
```

---

## 🔧 技术栈

| 组件               | 用途                                   |
| ---------------- | ------------------------------------ |
| **Python**       | 示例 Web 服务 demo_web.py                |
| **Docker**       | 应用镜像构建                               |
| **GitLab CI/CD** | 自动化流水线执行                             |
| **Fleet**        | 设备管理 / 配置同步                          |
| **NEU 扫描工具**     | 安全扫描（SAST / Dependency / Image Scan） |
| **Kustomize**    | Kubernetes 配置模板                      |

---

## 📁 项目结构

```
python_fleet/
├── kustomize/          # Kubernetes 部署模板（用于 Fleet 或 K8s 集群）
├── static/             # 静态资源
├── templates/          # 示例模板文件
├── demo_web.py         # Python 示例 Web 服务
├── dockerfile          # Docker 镜像构建定义
├── scan.yaml           # NEU 扫描配置文件
├── .gitlab-ci.yml      # GitLab CI 流水线配置
└── README.md           # 项目说明文档
```

---

## 🚀 快速开始

### 前置条件

* 具有 GitLab 项目权限
* 已连接 NEU 安全扫描服务
* 已部署 Fleet 平台（并具备 API Token 或访问凭证）
* Docker 环境（本地构建时需要）

---

## 🔨 本地运行 Python Web Demo

```bash
pip install flask
python demo_web.py
```

应用将默认在 `http://127.0.0.1:5000` 提供简单 Web 服务。

---

## 🐳 构建 Docker 镜像

```bash
docker build -t python_fleet_demo:latest .
```

如需运行：

```bash
docker run -p 5000:5000 python_fleet_demo
```

---

## 🛠 GitLab CI 流水线（.gitlab-ci.yml）

流水线阶段说明：

| Stage      | 步骤           | 说明                             |
| ---------- | ------------ | ------------------------------ |
| **lint**   | 代码检查         | 可扩展 flake8/Pylint              |
| **scan**   | NEU 安全扫描     | 使用 `scan.yaml` 配置 SAST/依赖/镜像扫描 |
| **build**  | 构建镜像         | 使用 Docker 构建 demo 应用           |
| **deploy** | Fleet 同步（可选） | 推送配置或触发设备策略同步                  |

你可根据企业内部 Registry / Fleet 接入方式，修改 `.gitlab-ci.yml` 中相关变量：

```yaml
FLEET_URL: "http://your-fleet-server"
NEU_SCAN_URL: "http://neu-scan-server"
```

---

## 🔍 NEU 安全扫描（scan.yaml）

`scan.yaml` 用于配置：

* 代码静态扫描（SAST）
* 依赖漏洞扫描
* Docker 镜像漏洞扫描
* 合规性检查（如 CIS 检查）

CI 中自动执行扫描并在作业日志中显示结果。

---

## 🖥️ Fleet 集成说明

本项目支持：

✔ 自动触发 Fleet 配置同步
✔ 扫描合规后再推送配置（Shift Left）
✔ 终端设备自动拉取最新策略 / 配置

可根据你的实际 Fleet 平台替换：

* API 地址
* 设备组
* 策略模板

---

## 📦 Kubernetes 部署（可选）

使用 `kustomize/` 中的模板：

```bash
kubectl apply -k kustomize/
```

这将部署 python_fleet Demo Web 服务（可与 Fleet / CI/CD 流程联动）。

---

## 🤝 贡献方式

欢迎参与项目改进：

* 提交 Issue
* 提交 PR（建议保持一致的代码风格）
* 优化 CI 流程 / 扩展安全扫描规则

---

## 📬 联系方式

如需协助或咨询：974177019@qq.com

* 邮箱：请在此填入你的邮箱
* GitLab 项目 Issue 讨论区

---

## 📝 License

本项目仅用于学习与演示 DevSecOps 流程，不用于生产环境。
可以自由 Fork / 修改 / 内部使用。

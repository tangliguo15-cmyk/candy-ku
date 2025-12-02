# 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制代码到容器
COPY . .

# 启动命令（用python3）
CMD ["python3", "-u", "api_server.py"]
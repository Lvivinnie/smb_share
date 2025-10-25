import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
# import sys
import json
import base64
import os.path
from PIL import ImageTk, Image
import base64
from io import BytesIO
import re
import ctypes
import subprocess
import sys

class SMBConnector:
    driver_letter = "X"
    def __init__(self, root):
        self.driver_letter = "X"
        self.root = root
        self.root.title("光高网络硬盘 v1.0.8")
        self.root.resizable(False, False)
        
            # 替换原有的图标路径获取和加载代码
        logoBase64 = 'data:image/x-icon;base64,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'
        # 前缀
        prefix = 'data:image/x-icon;base64,'
        # 去除前缀
        logoData = re.sub(f'^{prefix}', '', logoBase64)
        # 解码
        logoBytes = base64.b64decode(logoData)
        # 转为 Pillow 可读数据
        imageData = BytesIO(logoBytes)
        # Pillow 打开图像
        pillowImage = Image.open(imageData)
        # 转为 tkinter 图像
        tkinterImage = ImageTk.PhotoImage(pillowImage)
        # 设置 logo
        root.iconphoto(False, tkinterImage)


        
        self.config_file = self._get_config_path()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("微软雅黑", 10))
        self.style.configure("TButton", font=("微软雅黑", 10))
        self.style.configure("TEntry", font=("微软雅黑", 10))
        
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # -------------------------- 核心修改：共享路径改为二选一单选按钮 --------------------------
        ttk.Label(self.main_frame, text="访问:").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # 1. 创建变量存储选中的实际路径（而非显示文本，简化逻辑）
        self.selected_smb_path = tk.StringVar()
        # 2. 定义共享路径选项（显示文本, 实际路径）
        self.smb_options = [
            ("个人文件夹", r"\\10.32.10.17\personal_folder"),
            ("共享文件夹", r"\\10.32.10.17\共享文件夹")
        ]
        # 3. 用Frame包裹单选按钮，保证排版整齐
        self.radio_frame = ttk.Frame(self.main_frame)
        self.radio_frame.grid(row=3, column=1, sticky=tk.W, pady=5)  # 左对齐，与输入框对齐
        # 4. 创建两个单选按钮（互斥，绑定同一个变量）
        for idx, (text, path) in enumerate(self.smb_options):
            ttk.Radiobutton(
                self.radio_frame,
                text=text,
                variable=self.selected_smb_path,
                value=path,  # 变量存储实际路径
                style="TRadiobutton"
            ).grid(row=0, column=idx, padx=8)  # 两个按钮横向排列，间距15
        
        # 设置默认选中第一个选项（个人文件夹）
        self.selected_smb_path.set(self.smb_options[0][1])
        # ----------------------------------------------------------------------------------------
        
        # 用户名、密码等原有代码不变
        ttk.Label(self.main_frame, text="用户名:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.username = ttk.Entry(self.main_frame, width=40)
        self.username.grid(row=1, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="密码:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password = ttk.Entry(self.main_frame, width=40, show="*")
        self.password.grid(row=2, column=1, pady=5)
        
        self.remember_pwd = tk.BooleanVar()
        self.pwd_check = ttk.Checkbutton(self.main_frame, text="记住密码", variable=self.remember_pwd)
        self.pwd_check.grid(row=3, column=1, sticky=tk.E, pady=5)
        
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=15)
        
        self.connect_btn = ttk.Button(self.button_frame, text="登录", command=self.connect_smb, width=15)
        self.connect_btn.pack(side=tk.LEFT, padx=5)
        
        self.disconnect_btn = ttk.Button(self.button_frame, text="退出账号", command=self.disconnect_smb, width=15)
        self.disconnect_btn.pack(side=tk.LEFT, padx=5)
        self.disconnect_btn.config(state=tk.DISABLED)
        
        # 状态区域：补充grid布局（原代码漏了，导致状态框不显示）
        # ttk.Label(self.main_frame, text="v1.0.1").grid(row=6, column=2, sticky=tk.W)
        self.status_text = tk.Text(self.main_frame, width=40, height=8, wrap=tk.WORD)
        self.status_text.grid(row=7, column=0, columnspan=2, pady=5)
        self.status_text.config(state=tk.DISABLED)
        
        self.connected = False
        self.current_path = ""
        self.load_config()
        


        # -------------------------- 关键：窗口居中代码 --------------------------
        # 1. 先更新窗口布局，确保能获取到正确的窗口尺寸
        self.root.update_idletasks()
        # 2. 获取屏幕宽高
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # 3. 获取窗口宽高
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        # 4. 计算居中坐标（整数，避免窗口位置偏移）
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        # 5. 设置窗口位置（格式："宽x高+横坐标+纵坐标"）
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        # ------------------------------------------------------------------------

    # 以下方法仅修改与“路径选择”相关的逻辑，其他代码不变
    def _get_config_path(self):
        if os.path.exists("D:\\"):
            return "D:\\smb_config.json"
        return "smb_config.json"

    def on_close(self):
        self.save_config()
        # 使用更彻底的断开连接方法
        self.force_disconnect_all_smb()
        self.root.destroy()
    
    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def save_config(self):
        """保存配置：直接存储选中的实际路径，无需再存显示文本"""
        config_data = {
            "smb_path": self.selected_smb_path.get(),  # 存储实际路径（核心修改）
            "remember_pwd": self.remember_pwd.get(),
            "username": self.username.get().strip()
        }
        
        if self.remember_pwd.get() and self.username.get().strip():
            encoded_pwd = base64.b64encode(self.password.get().strip().encode()).decode()
            config_data["password"] = encoded_pwd
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, ensure_ascii=False, indent=4)
            self.update_status(f"配置已保存至: {self.config_file}")
        except Exception as e:
            self.update_status(f"保存配置失败: {str(e)}")
    
    def load_config(self):
        """加载配置：直接设置单选按钮的实际路径，无需匹配显示文本"""
        if not os.path.exists(self.config_file):
            return
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)

                # 恢复单选按钮选中状态（核心修改：直接设置实际路径变量）
                if "smb_path" in config_data and config_data["smb_path"]:
                    self.selected_smb_path.set(config_data["smb_path"])
                
                if "remember_pwd" in config_data:
                    self.remember_pwd.set(config_data["remember_pwd"])
                
                if "username" in config_data and config_data["username"]:
                    self.username.delete(0, tk.END)
                    self.username.insert(0, config_data["username"])
                
                if "password" in config_data and config_data["password"]:
                    try:
                        decoded_pwd = base64.b64decode(config_data["password"]).decode()
                        self.password.delete(0, tk.END)
                        self.password.insert(0, decoded_pwd)
                    except:
                        self.update_status("密码解码失败，可能是配置文件损坏")
                
            self.update_status(f"已加载配置文件: {self.config_file}")
        except Exception as e:
            self.update_status(f"加载配置失败: {str(e)}")
            
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def refresh_explorer(self):
        """刷新Windows资源管理器"""
        try:
            # 定义系统API所需的常量
            SHCNE_ASSOCCHANGED = 0x8000000  # 关联更改事件
            SHCNF_IDLIST = 0x0  # 以ID列表形式传递
            
            # 调用shell32.dll中的SHChangeNotify函数刷新资源管理器
            ctypes.windll.shell32.SHChangeNotify(
                SHCNE_ASSOCCHANGED,
                SHCNF_IDLIST,
                None,
                None
            )
            self.update_status("资源管理器已刷新")
        except Exception as e:
            self.update_status(f"刷新资源管理器失败: {str(e)}")

    def run_admin_command(self,command):
        """以管理员身份执行单个命令（仅在需要时）"""
        if self.is_admin():
            # 已为管理员，直接执行
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            return result.stdout + result.stderr
        else:
                   # 非管理员，临时提升权限执行（不生成临时文件，直接运行）
            # 直接执行命令，无需输出重定向
            hinstance = ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "cmd.exe", f'/c {command}', None, 0  # 0=隐藏命令窗口（可选1显示）
            )
            # 检查是否启动成功
            if hinstance <= 32:
                return f"命令执行失败：无法获取管理员权限（错误码：{hinstance}）"
            else:
                return "命令已请求管理员权限执行（无输出）"

    def reboot_workstation(self):
        result = self.run_admin_command('net stop Workstation /y & net start Workstation')
        import time
        time.sleep(2)
        # start_res = self.run_admin_command('net start Workstation')
        return result

    def connect_smb(self):
        """连接SMB：直接从单选按钮变量获取路径（核心修改，逻辑简化）"""
        path = self.selected_smb_path.get()  # 无需再通过显示文本匹配路径
        user = self.username.get().strip()
        pwd = self.password.get().strip()
        
        if not pwd:
            messagebox.showerror("错误", "请输入密码")
            return

        if not path:
            messagebox.showerror("错误", "请选择SMB共享路径")
            return
        
        self.save_config()
        
        # 在连接前先检查并清理现有连接
        self.run_command('net use * /delete /y', show_output=False)
        if user and pwd:
            command = f'net use {self.driver_letter}: "{path}" /user:{user} {pwd}'
        else:
            command = f'net use {self.driver_letter}: "{path}"'
        
        result = self.run_command(command)
        
        # 获取显示文本用于提示（仅为了用户友好，不影响路径逻辑）
        selected_text = next((opt[0] for opt in self.smb_options if opt[1] == path), "未知路径")
        if "成功" in result:
            self.connected = True
            self.current_path = path
            self.update_status(f"已成功连接到: {selected_text}")
            self.disconnect_btn.config(state=tk.NORMAL)
            self.open_smb()
        else:
            if "1219" in result:
                self.update_status("检测到错误代码1219...")
                try:
                    msg = self.reboot_workstation()
                    self.update_status(msg)
                    # 再次清理
                    msg = self.run_command('net use * /delete /y', show_output=False)
                    self.update_status(msg)

                    msg = self.run_command(command)
                    # 如果失败再次执行
                    if "67" in msg:
                        import time
                        time.sleep(1)
                        msg = self.run_command(command)
                    # 获取显示文本用于提示（仅为了用户友好，不影响路径逻辑）
                    selected_text = next((opt[0] for opt in self.smb_options if opt[1] == path), "未知路径")
                    if "成功" in msg:
                        self.connected = True
                        self.current_path = path
                        self.update_status(f"已成功连接到: {selected_text}")
                        self.disconnect_btn.config(state=tk.NORMAL)
                        self.open_smb()
                        return                
                except Exception as e:
                    self.update_status(f"重启服务时发生错误: {str(e)}")  
            elif "85" in result or "67" in result:
                self.update_status(f"出现错误码：{result}")
                self.run_admin_command('net start Workstation')
                import time
                time.sleep(3)
                self.run_command(command)
                self.connected = True
                self.current_path = path
                self.update_status(f"已成功连接到: {selected_text}")
                self.disconnect_btn.config(state=tk.NORMAL)
                self.open_smb()
                return
            else:             
                self.update_status(f"连接失败: {result}")
                messagebox.showerror("失败", f"连接SMB共享失败\n{result}")
    
    def open_smb(self):
        if not self.connected or not self.current_path:
            messagebox.showwarning("警告", "请先连接到SMB共享")
            return
        try:
            # target_path = self.current_path.replace("\\\\\\\\", "\\\\")
            # target_path = target_path.replace("17\\\\", "17\\")
            os.startfile(self.current_path)
            if "personal_folder" in self.current_path:
                self.refresh_explorer()  # 新增：刷新资源管理器

            # messagebox.showinfo("测试",target_path)
            selected_text = next((opt[0] for opt in self.smb_options if opt[1] == self.current_path), self.current_path)
            self.update_status(f"已打开共享文件夹: {selected_text}")
        except Exception as e:
            self.update_status(f"打开文件夹失败: {str(e)}")
            messagebox.showerror("失败", f"打开文件夹失败: {str(e)}")
    
    def disconnect_smb(self):
        # if not self.connected or not self.current_path:
        #     messagebox.showwarning("警告", "没有活跃的SMB连接")
        #     return
        
        selected_text = next((opt[0] for opt in self.smb_options if opt[1] == self.current_path), self.current_path)
        
        # 更彻底的断开连接方法
        self.force_disconnect_all_smb()
        
        self.connected = False
        self.update_status(f"已断开连接: {selected_text}")
        self.connect_btn.config(state=tk.NORMAL)
        self.disconnect_btn.config(state=tk.DISABLED)
        messagebox.showinfo("成功", f"已断开 {selected_text} 连接")
    
    def force_disconnect_all_smb(self):
        """强制断开所有SMB连接，解决系统残留连接问题"""
        try:
            self.update_status("正在清理SMB连接...")
            
            # 1. 使用net use清理所有连接
            self.run_command('net use * /delete /y', show_output=False)
            
            
            # 2. 检查是否还有PowerShell连接残留
            ps_check = self.run_admin_command('powershell -Command "Get-SmbConnection | Format-Table -AutoSize"', show_output=False)
            if "10.32.10.17" in ps_check:
                self.update_status("检测到PowerShell SMB连接残留，正在重启Workstation服务...")
                try:
                    # 停止Workstation服务
                    self.reboot_workstation()
                    # 再次清理
                    self.run_command('net use * /delete /y', show_output=False)
                    
                    # 最终验证
                    final_check = self.run_admin_command('powershell -Command "Get-SmbConnection | Format-Table -AutoSize"', show_output=False)
                    if "10.32.10.17" not in final_check:
                        self.update_status("SMB连接清理完成（已重启服务）")
                    else:
                        self.update_status("警告：仍有连接残留，可能需要重启计算机")
                except Exception as e:
                    self.update_status(f"重启服务时发生错误: {str(e)}")
            else:
                self.update_status("SMB连接清理完成")
                
        except Exception as e:
            self.update_status(f"清理SMB连接时发生错误: {str(e)}")
    
    def check_smb_connections(self):
        """检查当前SMB连接状态"""
        try:
            # 检查多种连接状态
            net_use_result = self.run_command('net use', show_output=False)
            net_session_result = self.run_command('net session', show_output=False)
            
            # 检查是否有任何相关连接
            has_connections = (
                "10.32.10.17" in net_use_result or 
                "10.32.10.17" in net_session_result or
                "personal_folder" in net_use_result.lower() or
                "共享文件夹" in net_use_result
            )
            
            if has_connections:
                self.update_status("检测到现有SMB连接，正在深度清理...")
                self.force_disconnect_all_smb()
                return False
            else:
                self.update_status("未检测到现有SMB连接")
                return True
        except Exception as e:
            self.update_status(f"检查SMB连接状态时发生错误: {str(e)}")
            return True
    
    def run_command(self, command, show_output=True):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                capture_output=True,
                text=True,
                startupinfo=startupinfo
            )
            
            output = result.stdout + result.stderr
            if show_output:
                self.update_status(f"命令执行结果: {output}")
            return output
        except subprocess.CalledProcessError as e:
            error = e.stdout + e.stderr
            self.update_status(f"命令执行错误: {error}")
            return error
        except Exception as e:
            self.update_status(f"执行命令时发生错误: {str(e)}")
            return str(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = SMBConnector(root)
    root.mainloop()
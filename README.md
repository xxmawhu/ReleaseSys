# ReleaseSys.git
这是邮件推送系统的初级版本。采用系统的mutt进行推送邮件，收件人用.mailList进行
存储， 默认的收件人列表在 ~/.mailList中。邮件的内容存在特定的文件Announce中。
* Announce的注释用"#"
* 设置主题用 
    subject= Draft | RealseSys
## 系统的使用方法为
* 初始化，每个文件夹只需要进行一次初始化，初始化的成功的标志为自动创建了文件
     Announce
      RealseSys init
*   发送
      RealseSys send
      或 RealseSys send -L mailLitFile
*   查看帮助 
      RealseSys -h 
      RealseSys -help
*   mutt的常用功能都能使用，比如
     *添加附件 -a file 

## mutt的基本设置
```bash
set realname="Group Repository"
set charset="utf-8"
set attach_charset="utf-8"
set send_charset="utf-8:us-ascii:iso-8859-1"
set config_charset="utf-8"
my_hdr From:maxx@ihep.ac.cn
```
建议把这些内容加入到 ~/.muttrc中

    


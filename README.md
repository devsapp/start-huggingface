
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-huggingface 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-huggingface&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-huggingface" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-huggingface&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-huggingface" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-huggingface&type=packageDownload">
  </a>
</p>

<description>

HuggingFace(fc3.0)

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-huggingface/tree/main)

</codeUrl>
<preview>

- [:eyes: 预览](https://github.com/devsapp/start-huggingface/tree/main)

</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |
| NAS |  AliyunNASFullAccess | [帮助文档](undefined) [计费文档](undefined) |
| VPC |  AliyunVPCFullAccess | [帮助文档](undefined) [计费文档](undefined) |

</service>

<remark>



</remark>

<disclaimers>

免责声明：   
本项目会将模型下载到NAS，并且使用函数计算的GPU实例，模型的大小会影响文件存储占用以及函数执行时间，需根据情况具验证模型下载及加载所产生的费用。

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-huggingface) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-huggingface) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-huggingface -d start-huggingface`
  - 进入项目，并进行项目部署：`cd start-huggingface && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例支持将huggingface各种开源模型，快速部署到阿里云函数计算FC，并提供相应的推理API服务。

Hugging Face 是一个旨在推动自然语言处理（NLP）技术和工具发展的开源社区和公司。他们致力于提供各种NLP任务中的最新技术、模型和工具，以及为开发者提供便捷的方式来使用、微调和部署这些技术。Hugging Face 在NLP领域中的贡献得到了广泛认可，成为了许多开发者和研究者的重要资源。除了自然语言处理，还支持处理图像和音频等多模态任务，社区还提供海量的预训练模型和数据集。

将huggingface模型部署至函数计算Serverless GPU具有以下优势：

a). 成本效益： Serverless 架构使得资源利用更加灵活，可以根据需求动态分配和释放资源，从而降低成本。利用 Serverless GPU，开发者可以根据实际需要分配 GPU 资源，而不必一直支付固定的 GPU 租用费用。

b). 弹性扩展： 在需求量增加时，Serverless GPU 能够自动扩展以满足更高的负载，而不会因为硬件限制导致性能瓶颈。这种弹性扩展使得系统能够更好地应对突发流量和高负载情况。

c). 简化管理： 使用 Serverless GPU，开发者无需关心底层硬件和软件的管理维护工作，如服务器配置、操作系统更新等。平台提供商负责管理基础设施，开发者只需专注于模型开发和部署。

d). 高可用性： Serverless GPU 架构通常具有高可用性，因为服务商会自动处理故障转移和容错机制。这样可以确保模型服务的持续可用性，提高系统稳定性和可靠性。

e). 灵活部署： Serverless GPU 可以根据应用程序的需求部署到不同的地理位置，以降低延迟和提高性能。同时，也可以轻松地跨多个云平台进行部署，提高了系统的灵活性和可移植性。

综上所述，将huggingface模型部署至 函数计算 GPU 上具有降低成本、弹性扩展、简化管理、高可用性和灵活部署等必要性，可以帮助开发者更高效地部署和管理模型服务。

</appdetail>

## 使用流程

<usedetail id="flushContent">

### huggingface配置

<img src="https://img.alicdn.com/imgextra/i2/O1CN01zDZtXt1mvq0VzlwXb_!!6000000005017-0-tps-1500-345.jpg">
其中主要涉及huggingface中的模型ID, 模型任务类型， 加载模型需要的库，已经huggingface access token， 下面以distilbert/distilbert-base-uncased-finetuned-sst-2-english为例，进入到模型详情页，https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
<img src="https://img.alicdn.com/imgextra/i4/O1CN01AKnqlW1iimFZejoRE_!!6000000004447-0-tps-1500-651.jpg">
模型ID,其中上图中标识1，即为模型ID<br>
模型任务类型, 其中上图中标识的2， 即为任务类型。模版中的认为类型需要映射下，具体映射规则见下表<br>
加载模型需要的库, 图中3位置即为需要加载的模型库，选择模版中的Transformers即可<br>
access token， 进入到https://huggingface.co/settings/tokens，页面获取即可<br>

### 详情
huggingface应用使用的huggingface提供的transformers和diffusers两个库进行模型加载，所以本身模型需要能支持这两个库进行加载才行。

#### transformers
如何确定模型能被transformers加载，可以进入到模型详情页，这里以distilbert/distilbert-base-uncased-finetuned-sst-2-english为例，如下图所示
<img src="https://img.alicdn.com/imgextra/i3/O1CN01LIBKR71PpD77tKdmA_!!6000000001889-0-tps-1500-716.jpg">
如上如所示，圈出位置有Transformers代表能用transformers进行加载，就可以使用函数计算提供的huggingface应用模版
##### 支持TASK列表
| Task Category                      | Task Identifier                     |
|------------------------------------|-------------------------------------|
| Audio Classification               | `audio-classification`              |
| Automatic Speech Recognition       | `automatic-speech-recognition`      |
| Text-to-Audio                      | `text-to-audio`                     |
| Text-to-Speech                     | `text-to-speech`                    |
| Depth Estimation                   | `depth-estimation`                  |
| Image Classification               | `image-classification`              |
| Image Segmentation                 | `image-segmentation`                |
| Image-to-Image                     | `image-to-image`                    |
| Object Detection                   | `object-detection`                  |
| Video Classification               | `video-classification`              |
| Zero-Shot Image Classification     | `zero-shot-image-classification`    |
| Zero-Shot Object Detection         | `zero-shot-object-detection`        |
| Fill-Mask                          | `fill-mask`                         |
| Question Answering                 | `question-answering`                |
| Summarization                      | `summarization`                     |
| Table Question Answering           | `table-question-answering`          |
| Text Classification                | `text-classification`               |
| Text Generation                    | `text-generation`                   |
| Text2Text Generation               | `text2text-generation`              |
| Token Classification               | `token-classification`              |
| Translation                        | `translation`                       |
| Zero-Shot Classification           | `zero-shot-classification`          |
| Document Question Answering        | `document-question-answering`       |
| Feature Extraction                 | `feature-extraction`                |
| Image Feature Extraction           | `image-feature-extraction`          |
| Image-to-Text                      | `image-to-text`                     |
| Mask Generation                    | `mask-generation`                   |
| Visual Question Answering          | `visual-question-answering`         |

#### diffusers
<font size=3>如何确定哪些模型能使用diffusers进行加载，以runwayml/stable-diffusion-v1-5为例，查看模型详情页
<img src="https://img.alicdn.com/imgextra/i1/O1CN01W0LUeL1Mw8Fg181WH_!!6000000001498-0-tps-1500-467.jpg">
如上图圈出有Diffusers标识的才可以使用</font>

##### 支持TASK列表
<font size=3>参考：https://huggingface.co/docs/diffusers/using-diffusers/pipeline_overview
<img src="https://img.alicdn.com/imgextra/i3/O1CN01lIKUcJ28R4xGmUndq_!!6000000007928-0-tps-1500-700.jpg">

| HuggingFace Task  | Model Task Identifier |
|--------------------|----------------------|
| Text-to-Image      | `text-to-image`      |
| Image-to-Image     | `image-to-image`     |
| Inpainting         | `inpainting`         |
| Depth-to-image     | `depth-to-image`     |

#### API
见：https://developer.aliyun.com/article/1476133

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>

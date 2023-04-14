import imageio

# imageio.imread() #从指定的文件读取图像。返回一个NUMPY数组,该数组带有元数据的元属性。
# t = imageio.mimread('/Users/cynthiashi/projects/nerf-pytorch/logs/room_test/room_test_spiral_200000_rgb.mp4')
t = imageio.mimread('/Users/cynthiashi/projects/nerf-pytorch/logs/blender_paper_lego/blender_paper_lego_spiral_200000_rgb.mp4')
print("图片个数：", len(t))

print("数据类型：", type(t[0]))           #打印数组数据类型  
print("数组元素数据类型：", t[0].dtype) #打印数组元素数据类型  
print("数组大小：", t[0].size)      #打印数组尺寸，即数组元素总数  
print("数组形状：", t[0].shape)         #打印数组形状  
print("数组的维度数目", t[0].ndim)      #打印数组的维度数目 
print("每个元素所占的字节数", t[0].itemsize)  #每个元素所占的字节数
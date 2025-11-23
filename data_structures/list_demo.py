# 列表基础操作示例
scores = [95, 88, 76, 100, 67]
print("原始列表：", scores)
print("最大值：", max(scores))
print("最小值：", min(scores))
print("平均分：", sum(scores) / len(scores))

# 排序（不会修改原列表）
sorted_scores = sorted(scores, reverse=True)
print("从高到低排序：", sorted_scores)

# 遍历
for i, s in enumerate(scores, start=1):
    print(f"第{i}个同学的分数：{s}")

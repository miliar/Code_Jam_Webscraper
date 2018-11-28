# usr/bin python
#-*- coding:utf-8 -*-

atoz = "abcdefghijklmnopqrstuvwxyz"
count,m,height,width,mapnum = 0,[],[],[],-1
for i,line in enumerate(open(r"D:\pgz\py\B-large.in")):
    if i == 0:
        t = int(line.strip())
    else:
        if count > 0:
            m[mapnum].append([int(l) for l in line.strip().split()])
            count -= 1
        else:
            mapnum += 1
            h,w = (int(l) for l in line.strip().split())
            height.append(h)
            width.append(w)
            m.append([])
            count = h

def areacheck(x,y,h,w):
    return 0<=x<h and 0<=y<w
def rep(flow,(x,y),ans):
    ans += [(x,y)]
    if (x,y) in flow:
        for x1,y1 in flow[(x,y)]:
            ans = rep(flow,(x1,y1),ans)
    return ans

f = open(r"D:\pgz\py\output.txt","w")
for i in range(t):
    sink,flow = [],{}
    for h in range(height[i]):
        for w in range(width[i]):
            xs,ys,xe,ye,xw,yw,xn,yn = h+1,w,h,w+1,h,w-1,h-1,w
            xf,yf = -1,-1
            z = m[i][h][w]
            if areacheck(xs,ys,height[i],width[i]):
                if z > m[i][xs][ys]:
                    z = m[i][xs][ys]
                    xf,yf = xs,ys
            if areacheck(xe,ye,height[i],width[i]):
                if z >= m[i][xe][ye] and m[i][h][w] > m[i][xe][ye]:
                    z = m[i][xe][ye]
                    xf,yf = xe,ye
            if areacheck(xw,yw,height[i],width[i]):
                if z >= m[i][xw][yw] and m[i][h][w] > m[i][xw][yw]:
                    z = m[i][xw][yw]
                    xf,yf = xw,yw
            if areacheck(xn,yn,height[i],width[i]):
                if z >= m[i][xn][yn] and m[i][h][w] > m[i][xn][yn]:
                    z = m[i][xn][yn]
                    xf,yf = xn,yn
            if xf== -1 and yf == -1:
                sink.append((h,w))
            else:
                if (xf,yf) in flow:
                    flow[(xf,yf)] += [(h,w)]
                else:
                    flow[(xf,yf)] = [(h,w)]
    area = []
    for (x,y) in sink:
        area.append(rep(flow,(x,y),[]))
    for ax in area:
        ax.sort()
    area.sort()
    alp = {}
    for j,ax in enumerate(area):
        for (x,y) in ax:
            alp[(x,y)] = atoz[j]
    f.write("Case #%(num)d:\n"%{"num":i+1})
    for h in range(height[i]):
        for w in range(width[i]):
            f.write(alp[(h,w)] + " ")
        f.write("\n")
f.close()
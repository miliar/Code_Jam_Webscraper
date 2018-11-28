#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <deque>
#include <set>
using namespace std;

typedef struct
{
    char color;
    int count;
}Record;
Record rec[6];
list<char> ans;

bool cmp(Record a,Record b)
{
    if (a.count<b.count) return true;
    return false;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_output_small.txt","w",stdout);
    int T;
    int N, R, O, Y, G, B, V;
    list<char>::iterator it;
    scanf("%d",&T);
    for (int index=1;index<=T;index++){
        ans.clear();
        scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
        rec[0].color='R'; rec[0].count=R;
        rec[1].color='Y'; rec[1].count=Y;
        rec[2].color='B'; rec[2].count=B;
        sort(rec,rec+3,cmp);
        //printf("2: %c %d\n",rec[2].color,rec[2].count);
        if (rec[2].count>rec[0].count+rec[1].count)
        {
            printf("Case #%d: IMPOSSIBLE\n",index);
            continue;
        }
        ans.clear();
        for (int i=0;i<rec[2].count;i++){
            ans.push_back(rec[2].color);
            if (rec[0].count>0){
                ans.push_back(rec[0].color);
                rec[0].count--;
            }else if (rec[1].count>0){
                ans.push_back(rec[1].color);
                rec[1].count--;
            }
        }
        if (rec[1].count>0){
            it = ans.begin();
            it++;
            while (it!=ans.end()){
                ans.insert(it,rec[1].color);
                rec[1].count--;
                if (rec[1].count==0) break;
                it++;
            }
        }
        printf("Case #%d: ",index);
        for (it = ans.begin();it!=ans.end();it++){
            printf("%c",*it);
        }
        printf("\n");
    }
    return 0;
}

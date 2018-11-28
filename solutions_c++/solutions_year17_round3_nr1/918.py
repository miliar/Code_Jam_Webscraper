#include <iostream>
#include <string.h>
#include<algorithm>
#include<stdio.h>
#include<math.h>
using namespace std;
double pai = acos(-1);
struct cake
{
    double r;
    double h;
    double area_s;
    double area_h;
    int no;
}p[1001];
bool cmp1(cake a ,cake b)
{
    return (b.area_s + b.area_h) < (a.area_s + a.area_h) ;
}
bool cmp2(cake a ,cake b)
{
    return (b.area_h) < (a.area_h) ;
}
int main() {
  int t,n,k;
  freopen("a.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for (int ii = 1; ii <= t; ++ii) {

    cin >> n>>k;
    for(int i=0;i<n;i++)
    {
        scanf("%lf%lf",&p[i].r,&p[i].h);
        p[i].no = i;
        p[i].area_s =p[i].r*p[i].r*pai;
        p[i].area_h =p[i].r*2*pai*p[i].h;
    }
    double max_ans =0;
    for(int j =0;j<n;j++){
        sort(p,p+n,cmp1);
        double ans = p[j].area_s + p[j].area_h;
        int used = p[j].no;
        sort(p,p+n,cmp2);
        int cnt_k=1;
        for(int i=0;i<n&&cnt_k<k;i++)
        {
            if(p[i].no == used)
                continue;
            cnt_k++;
            ans += p[i].area_h;
        }
        if(ans > max_ans)
            max_ans =ans;
    }
    printf("Case #%d: %.10lf\n",ii,max_ans);
  }
}

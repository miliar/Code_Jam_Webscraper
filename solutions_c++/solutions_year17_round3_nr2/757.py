#include<bits/stdc++.h>
using namespace std;
#define ll long long int
vector<int> C;
vector<int> J;
int main() {
  int t, AC,AJ,u,v,totalACTime,totalAJTime;
  //freopen("./in.txt", "r", stdin);
  //freopen("./out.txt", "w", stdout);
  scanf("%d", &t);
  for (int l=1;l<=t;l++) {
    scanf("%d %d", &AC, &AJ);
    totalACTime=0;
    totalAJTime=0;

    vector<int> day = vector<int>(2000, 0);

    for (int i=0;i<AC;i++)
    {
      scanf("%d %d",&u,&v);
      totalACTime += (v - u);
      for (int j=u;j<v;j++)
      {
        day[j]=1;
      }
    }
    for (int i=0;i<AJ;i++)
    {
      scanf("%d %d",&u,&v);
      totalAJTime += (v - u);
      for (int j=u;j<v;j++)
      {
        day[j]=2;
      }
    }

    int finalans=0;
    int k=0;
    while(day[k] == 0)
    {
      k++;
    }

    for (int j=k;j<k+1440;j++) {
      int day11=day[j % 1440];
      int day22=day[(j + 1) % 1440];
      if (day11 != day22)
      {
        int day1=day[j % 1440];
        int pos=j;
        while(day[(j + 1) % 1440] == 0)
        {
          j++;
        }
        int day2 = day[(j + 1) % 1440];
        if (day1 == day2)
        {
          if (day1 == 1)
          {
            C.push_back(j-pos);
          } else
          {
            J.push_back(j - pos);
          }
        } else {
          finalans++;
        }
      }
    }
    sort(C.begin(), C.end());
    sort(J.begin(), J.end());

    int szc=C.size();
    int szj=J.size();
    for (int j=0;j<szc;j++) {
      if ((C[j]+totalACTime) <= 720)
      {
        totalACTime += C[j];
      } else
      {
        finalans += 2;
      }
    }
    for (int j=0;j<szj;j++)
    {
      if ((J[j]+totalAJTime) <= 720)
      {
        totalAJTime += J[j];
      } else
      {
        finalans += 2;
      }
    }
    printf("Case #%d: %d\n", l, finalans);
    C.clear();
    J.clear();
  }
}

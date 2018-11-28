#include <bits/stdc++.h>
using namespace std;
FILE *fi;

int jat(int g)
{

fi=fopen("ez.txt","at");
long double d,h,l,s;
cin>>d>>h;
long double ma=1000000000000000000;
for (int i=0;i<h;i++)
{
    cin>>l>>s;
   long  double hh=(double) s+(s*l/(d-l));
    ma=min(ma,hh);
}
fprintf(fi,"Case #%d: %lf\n",g+1,ma);
fclose(fi);
  return 0;
}
int main()
{
fi=fopen("ez.txt","wt");
fclose(fi);
int n;

scanf("%d",&n);

for (int i=0;i<n;i++)
{

    jat(i);
}
        return 0;
}

//Indomie, Mie dari Indonesia
#include <bits/stdc++.h>
using namespace std;
typedef long double LD;
int tc,jarak,n;
LD timemaks,waktu,ans;
int main()
{
	freopen("InputCruiseBig.in","r",stdin);
	freopen("OutputCruiseBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%d%d",&jarak,&n);
		for(int i=1;i<=n;i++)
		{
			int posisi,kecepatan;
			scanf("%d%d",&posisi,&kecepatan);
			waktu=LD(jarak-posisi)/LD(kecepatan);
			if(i==1)
				timemaks=waktu;
			else
				timemaks=max(timemaks,waktu);
		}
		ans=LD(jarak)/timemaks;
		printf("Case #%d: %.10Lf\n",test,ans);
	}
}

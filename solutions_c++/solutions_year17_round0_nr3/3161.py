#include <iostream>
#include <cstdio>
using namespace std;
typedef long long LL;
int tc;
LL target,range,ans1,ans2;
void isi_ans(LL range){
	if(range%2==0)
		ans1=range/2,ans2=range/2-1;
	else
		ans1=range/2,ans2=range/2;
}
void cari_ans(LL gen,LL gan, LL totgen,LL totgan){
	//cout<<"hehe "<<gen<<" "<<gan<<endl;
	if(target<=totgen+totgan){
		int duluan;
		if(gan==-1||gen==-1)
		{
			if(gan==-1)
				duluan=0;
			else
				duluan=1;
		}
		else if(gen>gan)
			duluan=0;
		else
			duluan=1;
		if(duluan==0)
		{
			if(target<=totgen)
				isi_ans(gen);
			else
				isi_ans(gan);
		}
		else
		{
			if(target<=totgan)
				isi_ans(gan);
			else
				isi_ans(gen);
		}
		return;
	}
	target-=totgen+totgan;
	LL gen1=-1,gan1=-1,totgen1=0,totgan1=0;
	if(gen!=-1)
	{
		if((gen/2)%2==1)
			gan1=gen/2,gen1=gen/2-1;
		else
			gan1=gen/2-1,gen1=gen/2;
		totgan1+=totgen;
		totgen1+=totgen;
		if((gan/2)%2==1)
			totgan1+=2*totgan;
		else
			totgen1+=2*totgan;
	}
	else
	{
		if((gan/2)%2==1)
			totgan1+=2*totgan,gan1=gan/2;
		else
			totgen1+=2*totgan,gen1=gan/2;
	}
	cari_ans(gen1,gan1,totgen1,totgan1);
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("BathroomBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%lld%lld",&range,&target);
		if(range%2==1)
		{
			cari_ans(-1,range,0,1);
		}
		else
		{
			cari_ans(range,-1,1,0);
		}
		printf("Case #%d: %lld %lld\n",test,ans1,ans2);
	}
}

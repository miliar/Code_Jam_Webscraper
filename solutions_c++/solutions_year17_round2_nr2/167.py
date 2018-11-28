//Indomie, Mie dari Indonesia
#include <bits/stdc++.h>
using namespace std;
int total[10],tc,totalsemua;
vector <int> urutan;
bool valid,sudah[10];
int ubah(char a){
	if(a=='R')			//merah
		return 1;
	if(a=='Y')			//kuning
		return 2;
	if(a=='B')			//Biru
		return 3;
	if(a=='O')			//Orange
		return 6;
	if(a=='G')			//Green			Bergantung Pada Merah
		return 4;
	if(a=='V')			//Violet
		return 5;
}
char ubah(int a){
	if(a==1)
		return 'R';
	if(a==2)
		return 'Y';
	if(a==3)
		return 'B';
	if(a==4)
		return 'G';
	if(a==5)
		return 'V';
	if(a==6)
		return 'O';
}
int main()
{
	freopen("StableBig.in","r",stdin);
	freopen("StableBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%d%d%d%d%d%d%d",&totalsemua,&total[ubah('R')],&total[ubah('O')],&total[ubah('Y')],&total[ubah('G')],&total[ubah('B')],&total[ubah('V')]);
		valid=true;
		for(int i=1;i<=3;i++)
		{
			if(!((total[i+3]<total[i])||(total[i]==total[i+3]&&total[i+3]+total[i]==totalsemua)||(total[i]==0&&total[i+3]==0)))
				valid=false;
			total[i]-=total[i+3];
		}
		int temptotal=0,most=-1;
		for(int i=1;i<=3;i++)
		{
			temptotal+=total[i];
			most=max(most,total[i]);
		}
		if(temptotal-most<most)
			valid=false;
		if(!valid)
		{
			printf("Case #%d: IMPOSSIBLE\n",test);
			continue;
		}
		memset(sudah,false,sizeof(sudah));
		printf("Case #%d: ",test); 
		for(int i=1;i<=3;i++)
		{
			if(total[i+3]==0)
				continue;
			if(total[i]==0)
			{
				for(int ulang=1;ulang<=total[i+3];ulang++)
					printf("%c%c",ubah(i),ubah(i+3));
				goto lanjut;
			}
		}
		urutan.clear();
		int terbanyak,lain1,lain2;
		for(int i=1;i<=3;i++)
		{
			if(total[i]==most)
			{
				terbanyak=i;
				lain1=i%3+1;
				lain2=(i+1)%3+1;
			}
		}
		for(int i=1;i<=most;i++)
		{
			urutan.push_back(terbanyak);
			if(total[lain1]>=i)
				urutan.push_back(lain1);
			if(total[lain2]>=(most-i+1))
				urutan.push_back(lain2);
		}
		for(auto now:urutan){
			if(!sudah[now])
			{
				for(int ulang=1;ulang<=total[now+3];ulang++)
					printf("%c%c",ubah(now),ubah(now+3));
				sudah[now]=true;
			}
			printf("%c",ubah(now));
		}
		lanjut:
		printf("\n");
	}
}

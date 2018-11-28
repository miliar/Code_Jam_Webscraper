#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
using namespace std;
int tc,panjang;
long long input,ans;
vector <int> digit;
void convert_to_digit(long long angka){
	while(angka>0)
	{
		digit.push_back(angka%10);
		angka/=10;
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("outputTidyNumberBig.out","w",stdout);
	scanf("%d",&tc);
	for(int test=1;test<=tc;test++)
	{
		scanf("%lld",&input);
		digit.clear();
		convert_to_digit(input);
		ans=0;
		int batas=-1;
		for(int i=digit.size()-2;i>=0;i--)
		{
			if(digit[i]<digit[i+1])
			{
				batas=i+1;
				break;
			}
		}
		//cout<<"ini batas "<<batas<<endl;
		if(batas==-1)
			ans=input;
		else
		{
			while((batas!=digit.size()-1)&&!(digit[batas+1]<=digit[batas]-1))
				batas++;
			for(int i=digit.size()-1;i>batas;i--)
				ans=(long long) ans*10+digit[i];
			//cout<<"pertama "<<ans<<endl;
			ans=(long long) ans*10+digit[batas]-1;
			//cout<<"kedua "<<ans<<endl;
			for(int i=batas-1;i>=0;i--)
				ans=(long long) ans*10+9;
			//cout<<"ketiga "<<ans<<endl;
		}
		printf("Case #%d: %lld\n",test,ans);
	}
}

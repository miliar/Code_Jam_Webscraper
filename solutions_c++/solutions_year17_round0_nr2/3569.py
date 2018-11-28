//#define LOCAL
#include<iostream>
using namespace std; 
int main()
{
	#ifdef LOCAL
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out","w",stdout);
	#endif
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		char digits[20];
		cin>>digits;
		int iter = 0;
		int stopAc = 0;
		bool isAc = true;
		while (digits[iter]){
			if(iter!=0){
				if(digits[iter]>digits[iter-1] && isAc)
					stopAc=iter;
				if (digits[iter]<digits[iter-1])
					isAc=false;
			}
			iter++;
		}
		if(!isAc){
			digits[stopAc]-=1;
			iter=stopAc+1;
			while(digits[iter]){
				digits[iter]='9';
				iter++;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		iter=0;
		while(digits[iter]=='0')iter++;
		while(digits[iter]){
			cout<<digits[iter];
			iter++;
		}
		cout<<endl;
	}
	return 0;
}

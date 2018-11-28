#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,k,tmp,atm,t,test=1,flip;
	string s;
	cin>>t;
	while(t--){
		cin>>s>>k;
		atm=0;
		//cout<<"hell";
		cout<<"Case #"<<test<<": ";
		for (int i = 0; i < s.length();++atm)
		{
			// 	cout<<s<<" "<<i<<endl;
			for (; i < s.length() && s[i]=='+'; ++i);
			if (i>=s.length())
			{
				printf("%d\n",atm );
				break;
			}
		//	for (j=i; j < s.length() && s[j]=='-'; ++j);
			flip=k;
			if(i+flip>s.length()){
				printf("IMPOSSIBLE\n");
				break;
			}		//	cout<<flip;
			for (int tt=0,tm=i; tt < flip; ++tm,tt++)
			{
				//cout<<"here"<<tm<<endl;
				s[tm]=(s[tm]=='+')?('-'):('+');
			}
		}
		test++;
	}
	return 0;
}
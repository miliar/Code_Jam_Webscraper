#include<bits/stdc++.h>
using namespace std;
int n,r,o,y,g,b,v;
int R;
int Y;
int B;
bool ok;
char get(char last , char first){
	int a[6];
	a[0]=R;
	a[1]=max(R,Y);
	a[2]=Y;
	a[3]=max(Y,B);
	a[4]=B;
	a[5]=max(B,R);
	int z[6];
	z[0]=r;
	z[1]=o;
	z[2]=y;
	z[3]=g;
	z[4]=b;
	z[5]=v;
	char tmp[7]={'R','O','Y','G','B','V'};
	char res='$';
	int val=0;
	for(int i=0;i<6;i++)
	{
		if(z[i]==0)
		{
			continue;
		}
		if(tmp[i]==last)
		{
			continue;
		}
		if(a[i]>val)
		{
			val=a[i];
			res=tmp[i];
		}
		else if(a[i]==val)
		{
			if(tmp[i]==first){
				res=tmp[i];
			}
		}
	}
	if(res=='$'){
		ok=0;
	}
	if(res=='R'){
		--R;
		--r;
	}
	if(res=='O'){
		--R;
		--Y;
		--o;
	}
	if(res=='Y'){
		--Y;
		--y;
	}
	if(res=='G'){
		--Y;
		--B;
		--g;
	}
	if(res=='B'){
		--B;
		--b;
	}
	if(res=='V'){
		--B;
		--R;
		--v;
	}
	return res;
}
int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		R=0;
		Y=0;
		B=0;
		ok=1;
		R+=r;
		R+=o;
		R+=v;
		Y+=y;
		Y+=o;
		Y+=g;
		B+=b;
		B+=g;
		B+=v;
		char fst=get('$','$');
		char lst=fst;
		string res="";
		res+=fst;
		for(int i=2;i<=n;i++)
		{
			lst=get(lst,fst);
			res+=lst;
		}
		if(lst==fst){
			ok=0;
		}
		if(ok)
		{
			cout<<res<<endl;
		}
		else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
}
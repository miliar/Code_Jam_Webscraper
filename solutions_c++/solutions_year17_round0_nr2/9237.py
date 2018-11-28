/*
Name: Sushant Oberoi
MNNIT Allahabad
*/		
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sd(a) scanf("%d",&a)
#define slld(a) scanf("%lld",&a)
#define fl(i,a,b) for(int i=a;i<b;i++)
#define fle(i,a,b) for(int i=a;i<=b;i++)
#define fast ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)
#define wl(t) while(t--)
#define mod 1000000007
#define MAX 1000000
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int main()
{
	int t;
	sd(t);
	int x=1;
	wl(t){
	    printf("Case #%d: ",x++);
		string s;
		cin>>s;
		int len=s.length();
		for(int i=len-1;i>=0;){
			if(i-1>=0){
				if(s[i]=='0')
				{
				    int t=i+1;
				    while(t<len){
				        s[t]='9';
				        t++;
				    }
					while(i>=0 && s[i]=='0')
					{
						s[i]='9';
						i--;
					}
					if(s[i]=='1'){
						if(i==0)
							s[i]='x';
						else{
							while(i>=0 && s[i]=='1')
								{
									s[i]='9';
									i--;
								}
								if(i<0){
									s[0]='x';
								}
								else{
									s[i]='0'+((s[i-1]-'0')-1);
								}
						}
					}
					else{
					    s[i]='0'+((s[i]-'0')-1);
					}
				}
				else if(s[i]-'0'<s[i-1]-'0'){
					s[i]='9';
					if(s[i-1]!='0')
					{
					   s[i-1]='0'+((s[i-1]-'0')-1);
					   i--;
					}
					else{
					    i--;
					    while(i>=0 && s[i]=='0')
						{
							s[i]='9';
							i--;
						}
						if(s[i]=='1'){
							if(i==0){
								s[i]='x';
							}
							else{
								while(i>=0 && s[i]=='1')
								{
									s[i]='9';
									i--;
								}
								if(i<0){
									s[0]='x';
								}
								else{
									s[i]='0'+((s[i-1]-'0')-1);
								}
							}
						}
						else{
						 	s[i]='0'+((s[i-1]-'0')-1);
						}
					}
				}
				else
				  i--;
			}
			else
				i--;
		}
		int i=0;
		while(i<len && s[i]=='0'){
			s[i]='9';
			i++;
		}
		if(s[0]=='x')
		{
			s=s.substr(1,len-1);
		}
		len=s.length();
		fl(i,1,len){
		    if(s[i]-'0'<s[i-1]-'0'){
		        s[i]='9';
		    }
		}
		cout<<s<<endl;
	}
	return 0;
}
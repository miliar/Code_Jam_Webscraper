#include "iostream"
#include "cstdio"
#include "cstring"
#include "string"
using namespace std;
const int maxn=10;
int T,n;
typedef struct{
	int id,num;
}Node;
Node p[maxn];
int num[maxn];
bool cmp(Node x,Node y){
	return x.num>y.num;
}
string Ischar(int x){
	if(x==1)
		return "R";
	else if(x==3)
		return "Y";
	else
		return "B";
}
char Ischar1(int x){
	if(x==1)
		return 'R';
	else if(x==3)
		return 'Y';
	else
		return 'B';
}
int main()
{
	freopen("B-small-attempt3.in.txt", "r", stdin);  
    freopen("outb1.txt", "w", stdout);
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>n;
		for(int i=1;i<=6;i++){
			cin>>p[i].num;
			p[i].id=i;
		}
		printf("Case #%d: ",cas);
		sort(p+1,p+6+1,cmp);
		if(p[1].num>(p[3].num+p[2].num)){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			string s="";
			for(int i=0;i<p[1].num;i++)
				s+=Ischar(p[1].id);
			int pos=1;
			while(p[2].num){
				string ch=Ischar(p[2].id);
				s.insert(pos,ch);
				--p[2].num;
				pos+=2;
			}
			int len=s.length();
			for(int i=0;i<len;i++){
				if(s[i]==Ischar1(p[2].id))
					pos=i;
			}
			pos=(pos+2)%len;
			while(p[3].num){
				string tt=Ischar(p[3].id);
				s.insert(pos,tt);
				--p[3].num;
				int zz=s.length();
				pos=(pos+2)%zz;
			}
			cout<<s<<endl;
		}
	}
}
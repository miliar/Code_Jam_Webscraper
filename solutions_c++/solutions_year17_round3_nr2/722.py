#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;
struct line{
	int from,to;
	int belong;

}a[202],ta[1001],tb[1001],tc[1001];


bool cmp1(const line &a,const line &b){
	return a.from<b.from;
}
bool cmp2(const line &a,const line &b){
	int nowa = a.to-a.from;
	int nowb = b.to-b.from;
	return nowa<nowb;
}
int main()
{

	freopen("B-large.in","r",stdin);
	freopen("bbo","w",stdout);
	int T;
	cin>>T;
	int ac,aj;
	int timea,timeb;
	for(int cs=1;cs<=T;cs++){
		cin>>ac>>aj;
		timea=0,timeb=0;
		for(int i=0;i<ac;i++){
			cin>>a[i].from>>a[i].to;
			a[i].belong=1;
			timea+=a[i].to-a[i].from;

		}
		for(int i=ac;i<ac+aj;i++){
			cin>>a[i].from>>a[i].to;
			a[i].belong=2;
			timeb+=a[i].to-a[i].from;
		}

		sort(a,a+(ac+aj),cmp1);




		int pa=0,pb=0,pc=0;
		a[ac+aj].from = a[0].from+1440;
		a[ac+aj].belong = a[0].belong;
		for(int i=0;i<ac+aj;i++){

			int now = i;
			int next = i+1;

			if(a[now].belong == a[next].belong){
				if(a[now].belong==1){
					ta[pa].from = a[now].to;
					ta[pa].to = a[next].from;
					pa++;
				}
				else {
					tb[pb].from = a[now].to;
					tb[pb].to = a[next].from;
					pb++;
				}
			}
			else {
				tc[pc].from = a[now].to;
				tc[pc].to = a[next].from;
				pc++;
			}
		}
			sort(ta,ta+pa,cmp2);
			sort(tb,tb+pb,cmp2);

			int swith=0;
			//cout<<timea<<endl;
			//for(int i=0;i<pa;i++)
			//	cout<<ta[i].from<<" "<<ta[i].to<<endl;


			for(int i=0;i<pa;i++){
				timea+=ta[i].to-ta[i].from;
				//cout<<timea<<endl;
				if(timea>720)swith+=2;
			}
			for(int i=0;i<pb;i++){
				timeb+=tb[i].to-tb[i].from;
				if(timeb>720)swith+=2;
			}
			swith+=pc;



		cout<<"Case #"<<cs<<": "<<swith<<endl;

	}


	return 0;
}

#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class p {
public:
	int c;
	char col;
	int cc;
	int ok;
	int ff;
};

bool cmp(const p &i, const p &j) {
	if(i.ok != j.ok) return i.ok>j.ok;
	if(i.c!=j.c) return i.c>j.c;
	else if(i.ff!=j.ff) return i.ff>j.ff;
	else if(i.cc!=j.cc) return i.cc>j.cc;
	else return false;
}

p list[6];
int n;

bool pos(char a, char b) {
	if(a=='R') {
		return b!='R' && b!='O' && b!='V';
	} else if(a=='Y') {
		return b!='Y' && b!='O' && b!='G';
	} else if(a=='B') {
		return b!='B' && b!='G' && b!='V';
	} else if(a=='O') {
		return b=='B';
	} else if(a=='G') {
		return b=='R';
	} else if(a=='V') {
		return b=='Y';
	}
}

int main() {
	FILE* in=fopen("B-small-attempt4.in","rt");
	FILE* out=fopen("Bout.txt","wt");
	int t;
	fscanf(in,"%d",&t);
	//scanf("%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		//printf("Case #%d: ",tc);
		fscanf(in,"%d",&n);
		//scanf("%d",&n);
		for(int i=0;i<6;i++) {
			fscanf(in,"%d",&list[i].c);
			//scanf("%d",&list[i].c);
		}
		list[0].col='R'; list[1].col='O';
		list[2].col='Y'; list[3].col='G';
		list[4].col='B'; list[5].col='V';
		string res="";
		char pre;
		for(int i=0;i<6;i++)
			list[i].ok=1;
		for(int i=0;i<6;i++)
			list[i].cc=i%2;
		sort(list,list+6,cmp);
		res+=list[0].col;
		pre=list[0].col; list[0].c--;
		char fst=list[0].col;
		while(res.size()<n) {
			bool ok=false;
			for(int i=0;i<6;i++) {
				if(list[i].c>0 && pos(pre,list[i].col)) {
					ok=true; list[i].ok=1;
				} else list[i].ok=0;
				if(!pos(list[i].col,fst)) list[i].ff=1;
				else list[i].ff=0;
			}
			if(!ok) break;
			sort(list,list+6,cmp);
			res+=list[0].col;
			list[0].c--;
			pre=list[0].col;
		}
		if(res.size()<n) {
			fprintf(out,"IMPOSSIBLE\n");
			//printf("IMPOSSIBLE\n");
		} else {
			bool ok=true;
			for(int i=0;i<res.size();i++) {
				if(!pos(res[i],res[(i+1)%n])) {
					ok=false;
					fprintf(out,"IMPOSSIBLE\n");
					//printf("IMPOSSIBLE\n");
					break;
				}
			}
			if(ok) {
				char buf[1002];
				for(int i=0;i<res.size();i++)
					buf[i]=res[i];
				buf[res.size()]=0;
				fprintf(out,"%s\n",buf);
				//printf("%s\n",buf);
			}
		}
	}
	return 0;
}

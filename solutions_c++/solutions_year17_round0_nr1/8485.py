#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <iomanip>
#include <unordered_map>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define INF (1<<29)

unordered_map<string,int> myMap;

int getMin(string s,int n,int k)
{
	int ret=INF;
	int i,j;
	bool isdone=true;
	REP(i,n) if(s[i]!='+') { isdone=false; break; }
	if(isdone)
		ret=0;
	else{
		unordered_map<string,int>::const_iterator got=myMap.find(s);
		if(got == myMap.end()){
			REP(i,n-k+1){
				myMap.insert(pair<string,int>(s,INF));
				REP(j,k) s[i+j]=(s[i+j]=='+')?'-':'+';
				int tmp=getMin(s,n,k);
				REP(j,k) s[i+j]=(s[i+j]=='+')?'-':'+';
				if(tmp!=INF && (tmp+1)<ret){
					ret=tmp+1;
					myMap.erase(s);
					myMap.insert(pair<string,int>(s,ret));
				}
			}
		}
		else{
			if(ret>got->second)
				ret=got->second;
		}
		//printf("ans for %s = %d\n", s.c_str(), ret==INF?-1:ret);
	}
	return ret;
}

void main2(void){
	myMap.clear();
	string s;
	getline(cin>>ws, s);
	char* seq=strtok((char*)s.c_str()," ");
	string sequence=seq;
	seq=strtok(NULL," ");
	int k=stoi(seq);
	int n=sequence.size();
	int ans=getMin(sequence,n,k);
	if(ans==INF)
		gout<<"IMPOSSIBLE"<<endl;
	else
		gout<<ans<<endl;
}

int main(void){
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	REP(i,number_of_test_cases) main2();
	return 0;
}

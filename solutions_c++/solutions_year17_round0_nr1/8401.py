#include <bits/stdc++.h>
using namespace std;
typedef double ld;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int,int>ii;
const int MAXN=1111;
const int INF=0x7f7f7f7f;
int cases;

typedef unsigned long long ull;
struct Bitset{
    uint o;
    Bitset(){o=0;}
    Bitset(uint _o):o(_o){}
    
    void set(){o=-1;}//全置为1
    void reset(){o=0;}//全置为0
    void flip(){o^=-1;}//取反
    void set1(uint p){o|=(1<<p);}//把某位设为1
    void set0(uint p){o&=~(1<<p);}//把某位设为0
    bool at(uint p)const{return (o>>p)&1;}//某位

    void flip(uint p){//把某位取反
        if(at(p)) set0(p);
        else      set1(p);
    }
    int left0(){return __builtin_clz(o);}//前导(左)0的个数,o=0时结果未定义
    bool operator[](uint p){return at(p);}
    bool operator <(const Bitset& that)const{
    	return o<that.o;
    }
    void write(){for(auto i=63-left0();i>=0;i--){cout<<at(i);}cout<<'\n';}
    //void write(int p){for(auto i=p-1;i>=0;i--){cout<<at(i);}cout<<'\n';}
    void write(int p)const{for(auto i=0;i<p;i++)cout<<at(i);}
};//低位从0开始计数

void gao(Bitset t,int x,int k){
	Bitset bb=0;
	for(int i=0;i<x;i++){
		bb.set1(i);
	}

	map<Bitset,int>ans;
	queue<pair<Bitset,int> >q;

	q.push(make_pair(bb,0));
	while(!q.empty()) {
	    auto now=q.front(); q.pop();
	    ans[now.first]=now.second;

	    for(int i=k-1;i<x;i++){
	    	auto v=now.first;
	    	for(int j=k,p=i;j>0;j--,p--){
	    		v.flip(p);
	    	}
	    	
	    	if(!ans.count(v)){
	    		q.push(make_pair(v,now.second+1));
	    	}
		}
	}
	if(!ans.count(t)){
		printf("IMPOSSIBLE\n");
	}else printf("%d\n",ans[t]);
/*
	for(const auto& t:ans){
		t.first.write(x);
		cout<<' '<<t.second<<'\n';
	}
*/
}



int main() {
	
	string str;
	int n,k;
	while(~scanf("%d",&cases)) {
	    for(int ca=1;ca<=cases;ca++){
	    	cin>>str>>k;
	    	printf("Case #%d: ",ca);
	    	uint now=0;
	    	for(int i=str.length()-1;i>=0;i--){
	    		now<<=1;
	    		if(str[i]=='+') now|=1;
	    	}
	    	Bitset nn=now;
	    	gao(nn,str.length(),k);
	    }
	}
	//*/
	/*
	#ifndef ONLINE_JUDGE 
	freopen("/Users/Corn/Desktop/out.txt", "w" ,stdout);
	#endif//ONLINE_JUDGE
	for(int i=2;i<=10;i++){
		for(int k=2;k<=i;k++){
			printf("%d %d\n",i,k);
			gao(i,k);
			printf("\n");
		}
	}
	*/
}

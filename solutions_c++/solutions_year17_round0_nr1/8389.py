#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int T,kase=1,k;
int len;
string s;
bitset<1111> bits;
int stat;

struct Node
{
	bitset<1111> bits;
	int step;
	Node(){bits.reset();step=0;};
	Node(bitset<1111> bits,int step):bits(bits),step(step){}
};

unordered_map<bitset<1111>,int> vis;

int bfs()
{
	queue<Node> q;
	Node t;
	q.push(Node(bits,0));
	while(!q.empty()){
		t=q.front();
		q.pop();
		if(vis[t.bits])
			continue;
		if(t.bits.count() == len)
		{
			//cout << t.bits << endl;
			return t.step;
		}
		vis[t.bits]=1;
		bitset<1111> tmp;
		for(int i=0;i<len-k+1;i++)
		{
			tmp=t.bits;
			for(int j=i;j<i+k;j++)
				tmp.flip(j);
			//cout << tmp << endl<<endl;;
			q.push(Node(tmp,t.step+1));
		}
	}
	return -1;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
#endif
	scanf("%d",&T);
	while(T--){
		vis.clear();		
		bits.reset();
		stat = 0;
		cin >> s >> k;
		len=s.size();
		for(int i=0;i<len;i++){
			if(s[i]=='+')
				bits.set(i);
		}
		stat = bfs();
		if(bits.count()==len){
			printf("Case #%d: %d\n",kase++,0);
		}
		else if(stat == -1){
			printf("Case #%d: IMPOSSIBLE\n",kase++);
		}
		else{
			printf("Case #%d: %d\n",kase++,stat);
		}
	}
	return 0;
}

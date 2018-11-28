#include <stdio.h>
#include <algorithm>
#include <queue>
#include <map>

struct node {
	int ad,hd,ak,hk;
	node() {}
	node(int ad,int hd, int ak,int hk) 
	:ad(ad),hd(hd),ak(ak),hk(hk){}
	node& operator=(const node &rhs) {
		ad=rhs.ad; hd=rhs.hd; ak=rhs.ak; hk=rhs.hk;
		return *this;
	}
};
struct cmp_node {
	bool operator()(const node &a, const node &b) {
		if(a.ad!=b.ad) return a.ad<b.ad;
		else if(a.hd!=b.hd) return a.hd<b.hd;
		else if(a.ak!=b.ak) return a.ak<b.ak;
		else return a.hk<b.hk;
	}
};

int main() {
	int test;
	scanf("%d", &test);
	for(int tc=1;tc<=test;tc++) {
		int hd, ad,hk,ak,b,d;
		scanf("%d %d %d %d %d %d",&hd,&ad,&hk,&ak,&b,&d);
		
		node st(ad,hd,ak,hk);
		std::map<node, int, cmp_node> vis;
		vis[st]=1;
		std::queue<node> que;
		que.push(node(ad,hd,ak,hk));

		int or_hd=hd, or_hk=hk;

		int num=-1;
		while(!que.empty()) {
			node tmp=que.front(); que.pop();
			int now_num=vis[tmp];

			ad=tmp.ad; hd=tmp.hd; ak=tmp.ak; hk=tmp.hk;
			hk-=ad;
			if(hk<=0) {
				num=now_num;
				break;
			}
			hd-=ak;
			if(hd>0){
				node next(ad, hd,ak,hk);
				if(vis[next]==0) {
					// printf("%d : [%d %d %d %d]\n",now_num,ad,hd,ak,hk);
					vis[next]=now_num+1;
					que.push(next);
				}
			}

			ad=tmp.ad; hd=tmp.hd; ak=tmp.ak; hk=tmp.hk;
			ad+=b; hd-=ak;
			if(hd>0 && ad-b<or_hk) {
				node next(ad, hd,ak,hk);
				if(vis[next]==0) {
					// printf("%d : [%d %d %d %d]\n",now_num,ad,hd,ak,hk);
					vis[next]=now_num+1;
					que.push(next);
				}
			}

			ad=tmp.ad; hd=tmp.hd; ak=tmp.ak; hk=tmp.hk;
			ak-=d; 
			if(ak<0) ak=0;
			hd-=ak;
			if(hd>0) {
				node next(ad, hd,ak,hk);
				if(vis[next]==0) {
					// printf("%d : [%d %d %d %d]\n",now_num,ad,hd,ak,hk);
					vis[next]=now_num+1;
					que.push(next);
				}
			}

			ad=tmp.ad; hd=tmp.hd; ak=tmp.ak; hk=tmp.hk;
			hd=or_hd; hd-=ak;
			if(hd>0) {
				node next(ad, hd,ak,hk);
				if(vis[next]==0) {
					// printf("%d : [%d %d %d %d]\n",now_num,ad,hd,ak,hk);
					vis[next]=now_num+1;
					que.push(next);
				}
			}
		}
		printf("Case #%d: ",tc);
		if(num==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",num);
	}
	return 0;
}
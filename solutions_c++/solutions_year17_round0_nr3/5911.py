#include<iostream>
using namespace std;
struct node{
	long long d;
	node *next;
};
int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long n,k;
		cin>>n>>k;
		node *r = new node;
		r->d = n;
		r->next = NULL;
		for(int j=0;j<k;j++){
			node *tmp=r;
			//cout<<"printing list: ";
			//while(tmp!=NULL){
			//	cout<<tmp->d<<" ";
			//	tmp=tmp->next;
			//}
			node *maxn = r;
			tmp = r;
			node *tmp2=NULL;
			node *maxn2 = NULL;
			long long max=r->d;
			while(tmp!=NULL){
				if(max<tmp->d){
					maxn2=tmp2;
					max=tmp->d;
					maxn=tmp;
				}
				tmp2 =tmp;
				tmp = tmp->next;
			}
			node *x = new node;
			node *y = new node;
			x->d = (maxn->d)/2;
			y->d = ((maxn->d)-1)/2;
			x->next=r;
			y->next=x;
			r = y;
			if(maxn2!=NULL){
				maxn2->next = maxn->next;
			}else{
				x->next = maxn->next;
			}
			
			//cout<<"\n";
			delete maxn;
		}
		cout<<"Case #"<<i<<": "<<r->next->d<<" "<<r->d<<"\n";
		node *tmp=r;
		node *todel;
		//cout<<"printing list: ";
		while(tmp!=NULL){
			//cout<<tmp->d<<" ";
			todel = tmp;
			tmp=tmp->next;
			delete todel;
		}
	}
	return 0;
}

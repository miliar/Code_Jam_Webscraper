#include<bits/stdc++.h>
#define ll long long int
using namespace std;
string s;
struct Node{
	int index;
	int L;
	int R;
};
int getLs(int index){
	int count=0;
	for(int i=index-1;i>=1;i--){
		if(s[i]=='0'){
			count++;
		}else{
			break;
		}
	}
	return count;
}

int getRs(int index){
	int count=0;
	for(int i=index+1;i<=s.size()-2;i++){
		if(s[i]=='0'){
			count++;
		}else{
			break;
		}
	}
	return count;
}
int main()
{  
    int T,N,K;
    scanf("%d",&T);
   
    for(int t=1;t<=T;t++){
    	scanf("%d %d",&N,&K);
    	int y,z;
        s="";
    	for(int i=1;i<=N+2;i++){
    		if(i==1 || i==N+2){
    			s=s+"1";
			}else{
				s=s+"0";
			}
		}
	
	     
	    for(int i=1;i<=K;i++){
	    	
	    	vector<Node> p,q;
	    	int ma_mi=0,ma_ma=0;
	    	for(int j=1;j<=N;j++){
	    		if(s[j]=='0'){
	    		   int Ls=getLs(j);
	    		   int Rs=getRs(j);
	    		   ma_mi=max(ma_mi,min(Ls,Rs));
	    		   Node node={j,Ls,Rs}; 
				   p.push_back(node);	
				}    		
			}
	    	
	    	for(int j=0;j<p.size();j++){
	    		int val=min(p[j].L,p[j].R);
	    		if(ma_mi==val){
	    		   ma_ma=max(ma_ma,max(p[j].L,p[j].R));	
	    		   Node node={p[j].index,p[j].L,p[j].R}; 
				   q.push_back(node);
				}
			}
		   
		    if(q.size()==1){
				int ii=q[0].index;
				s[ii]='1';
				if(i==K){
				   y=max(q[0].L,q[0].R);
				   z=min(q[0].L,q[0].R);	
				}
			}else{
				
			    Node ma_node;
				for(int j=0;j<q.size();j++){
	    		    int val=max(q[j].L,q[j].R);
	    		    if(ma_ma==val){
	    		        ma_node={q[j].index,q[j].L,q[j].R}; 
				        break;
				    }
			    }
				
				int ii=ma_node.index;
				s[ii]='1';
				if(i==K){
				   y=max(ma_node.L,ma_node.R);
				   z=min(ma_node.L,ma_node.R);	
				}
				
			}
	       
		}
		   
    	printf("Case #%d: %d %d\n",t,y,z);
	}
   return 0;   
}


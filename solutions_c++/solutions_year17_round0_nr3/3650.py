#include <bits/stdc++.h>

using namespace std;

typedef vector<double> vi;
typedef priority_queue<double> pq;

void resposta(double val){
	/*long long int x = val;
	cout << val << "ex " << ex << endl;
	if(val==1) cout << "1 0" << endl;
	else{
		if(x == val ) {
			if(ex==0)
				cout << val << " " << val-1 << endl;
			else
				cout << val-1 << " " << val-1 << endl;
			
		}
		else{
			if(ex==0)
				cout << x << " " << x << endl;	
			else
				cout << x << " " << x-1 << endl;	
		}
	}*/
	long long int x = val;
	if(val==1) cout << "1 0" << endl;
		else{
		if(val==x){	
			cout << val << " " << val-1 << endl;
		}	
		else{
			cout << x << " " << x << endl;	
		}
	}
}


int main(){
	
	int t;
	long long int n,k,p,aux,cont,r1;
	double p2;	
	vi v;
	pq q;
	bool flag;
	cin >> t;

	for(int i=0;i<t;i++){
		
		cin >> n >> k;	
		p=0;
		r1=0;
		flag=true;
		//q.push(n);
		q.push(floor(n)/2.0);
		v.push_back(n);
		//v.push_back(floor(n)/2.0);
		while(1){		
				p = floor(q.top());
				
				//cout << p << " a " << q.top() << endl;
			
				
				
				if(q.top()==2){
					q.push(1);
				}
				else if(p == q.top()){
					q.push(p/2.0);
					q.push((p-1)/2.0);
					//cout << "push " << (p)/2.0 << " "<< (p-1)/2.0 << endl; 
	
				}
				else if (p != q.top()){ // fracionario
					q.push(p/2.0);
					q.push(p/2.0);	
					//cout << "push " << p/2.0 << " "<< p/2.0 << endl; 
				}
				
				v.push_back(q.top());
			        q.pop();		
				if(p <= 0) break; 		
			}
		//if(n%2==0)
		//v.push_back(1);
		/*for(int g=0;g<v.size();g++){
					cout << v[g] << " ";		
				}
			cout << endl;
		*/
		cout << "Case #"<< i+1 <<": ";
		//cout << r1 << endl;
		//long long int tam = n/log(r1);
		//long long int tam = 1+ r1+ r1/2;
		//cout << tam << endl;
		//int exp=0;
		if(k>v.size()-1) cout << "0 0" << endl;
		else resposta(v[k]);	
		//if(k >= tam){ cout << "0 0" << endl; }
		/*else{
			while(1){
			
				if(k == pow(2,exp)){
					resposta(v[exp+1],0);
					break;			
				}
				else if (k < pow(2,exp)){
					resposta(v[exp],1);
					break;		
				}
				exp++;
			}
		}*/
		v.clear();
		q = priority_queue <double>();
		
		}	
	

	return 0;
}	

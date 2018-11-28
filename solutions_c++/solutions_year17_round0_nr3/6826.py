
#include <bits/stdc++.h>
#include <cstring>

using namespace std;

int full[1000002];

void separar (int &N, int &K){
	 char s[13];
	 int m;
	   gets(s);
	   int j=0;
	   m=(int)s[0];
	
	   while(m !=32){
		 N=10*N + m -48;
		 j++;
		 m=(int)s[j];
    	}
    	
	   j++;
  	   m=(int)s[j];
  	   
    	while(j<strlen(s)){
		  K=10*K +m-48;
	    	j++;
	     m=(int)s[j];
    	}
    	
}

void insert(int x, int m){
	int i=0;
	while(i<m){
		if(x < full[i]){
			for(int j=m-1;j>=i; j--){
				full[j+1]=full[j];
			}
			full[i]=x;
			break;
		}
		i++;
	}
	
	if(i==m) full[i]=x;
	
}

void llenado(int N, int K){
	full[0]=0;
	full[1]=N+1;
	int cont=2;
	int i,num,ind,max,min,dif1,dif2,max_temp,min_temp;
	
	 
	while(K>0){
		i=0;
		max=0;
		
		while(i<cont-1){
			num=(full[i]+full[i+1])/2;
			dif1=abs(num-full[i+1]);
			dif2=abs(num-full[i]);
			max_temp=  (dif1 > dif2) ? dif1 : dif2;
			min_temp=  (dif1 > dif2) ? dif2: dif1;
			if(max< max_temp){
				max=max_temp;
				min=min_temp;
				ind=num;
			} else{
				if(max==max_temp){
					if(min_temp > min){
						max=max_temp;
				        min=min_temp;
				        ind=num;
					} else {
						if(min_temp==min){
							if(num<ind){
									max=max_temp;
				                   min=min_temp;
				                  ind=num;
							}
						}
					}
				}
			}
			i++;
		}
		if(K==1) break;
		insert(ind,cont);
		cont++;
		K--;
	}
	
	cout << max-1 << " " << min-1 << endl;
}

int main(){


	char c[3];
	
	gets(c);
	int T=0;
	int m=strlen(c);
	int j=0;
	while(j<m){
		T=10*T+(int)c[j]-48;
		j++;
	}
	
	for(int i=1; i<=T; i++){
		int N=0;
    	int K=0;
	
		separar(N,K);
		cout << "Case #" << i << ": ";
		llenado(N,K);
	}


return 0;
}


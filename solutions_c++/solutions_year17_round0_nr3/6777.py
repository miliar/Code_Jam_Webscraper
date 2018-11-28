#include<stdio.h>
#include<iostream>
#include<string>
#include<sstream>
using namespace std;
void print(int A[1000],int n){
	int i;
	for (i=1;i<=n;i++){
		cout<<A[i]<<" ";
	}
	cout<<"\n";
}
int minmax(int A[1000],int B[1000],int Main[1000],int z1,int k1,int n){
	int i,max1,max2,max[1000],j,k,z;
	max1 = A[1];
//	max2 = A[1];
	for(i=2;i<=n;i++){
		if(max1<=A[i] && Main[i]==0){
			max1 = A[i];
		}
	}
//	cout<<"max "<<max1 << endl;
	int p=1;
	for(i=1;i<=n;i++){
		if(A[i] == max1 && Main[i]==0){
			max[p] = i;
			p=p+1;
		}	
	}
	
	max[p] = 0;
//	print(max,p);
//	cout<<"p"<<" "<<p<<endl;
	if(p==2){
		Main[max[1]] = 1;
//		cout << max[1] << endl; ;
		return max[1];
	}
	else{
		max2 = B[max[1]];
		int k = max[1];
//		cout << k << endl;
		for(j=2;j<=p;j++){
			if(max2<B[max[j]]){
				max2 = B[max[j]];
				k = max[j];
			}
		}
		Main[k] = 1;
//		cout << k << endl;
		return k;
	}
/*	if(z1==k1){
		return k;
		cout<< A[k] << " ";
		cout<< B[k] << endl;
	}*/
}
int main(){
	int test,l2;
	cin >> test;
	for(l2=1;l2<=test;l2++){
		int A[1000],k,z,i,j,cl,cr,L[1000],R[1000],n,M[1000],Ma[1000];
		cin >> n ;
		cin >> k;
		for (i=1;i<=n;i++){
			A[i] = 0;
		}
		for(z=1;z<=k;z++){
//		cout<<"Main"<<endl;
//		print (A,n);
			for (i=1;i<=n;i++){
				cl=0;
				for (j=i-1;j>=1;j--){
					if(A[j]==1){
						break;
					}
					else{
						cl=cl+1;
					}
				}
				L[i] = cl;
				cr=0;
				for (j=i+1;j<=n;j++){
					if(A[j]==1){
						break;
					}
					else{
						cr=cr+1;
					}
				}
				R[i] = cr;
			}
			for(i=1;i<=n;i++){
				if(L[i]<R[i]){
					M[i] = L[i];
					Ma[i] = R[i];
				}
				else{
					M[i] = R[i];
					Ma[i] = L[i];
				}
			}		
			
//		print(L,n);
//		print(R,n);
//		print(M,n);
//		print(Ma,n);	
			int l1 = minmax(M,Ma,A,z,k,n);
//		cout << l1;
//		cout << "abhi";
			if(z==k){
//			print(A,n);
//			print (Ma,n);
//			print (M,n);
//			cout << l1 << endl;
				cout << "Case #"<< l2 << ": ";
				cout<< Ma[l1] << " ";
//			cout << "aks";
				cout<< M[l1] << endl;
			}
		}
	}
}

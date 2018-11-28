#include <iostream>
using namespace std;

void value_updater(long & k,long& alpha, long& beta,long& n1, long& n2);
void if_found(long & k, long & alpha, long & beta, long & n1, long & n2);
void even_splitter(long & k, long & alpha, long & beta, long & n1, long & n2);
void odd_splitter(long & k, long & alpha, long & beta, long & n1, long & n2);

int main(){
	int t;
	cin>>t;
	long n;
	long k;
	for(int i=0;i<t;i++){
		cin>>n>>k;
		long alpha=0;
		long beta=0;
		long n1=0;
		long n2=0;
		if (k==1){
			alpha = (n-1)/2;
			beta = n/2;
		}
		else if (n%2) {
			alpha = n;
			n1 = 1;
			odd_splitter(k, alpha, beta, n1, n2);
		}
		else {
			beta = n;
			n2 = 1;
			even_splitter(k, alpha, beta, n1, n2);
		}
		cout<<"Case #"<<i+1<<": "<<beta<<" "<<alpha<<endl;
	}
}
void even_splitter(long & k, long & alpha, long & beta, long & n1, long & n2){
	if (k<=n2) return if_found(k, alpha, beta, n1, n2);
	k-=n2;

	if(((beta -1)/2)%2){
		alpha = ((beta -1)/2);
		beta/=2;
		n1=n2;
		return value_updater(k,alpha, beta, n1, n2);
	}
	else {
		alpha = beta/2;
		beta = ((beta -1)/2);
		n1 = n2;
		return value_updater(k,alpha, beta, n1, n2);
	}
}

void odd_splitter(long & k, long & alpha, long & beta, long & n1, long & n2){
	if (alpha == 1) {
		alpha = 0;
		beta = 0;
		return;
	}
	else if (((alpha-1)/2)%2) {
		if (k<=n1) return if_found(k, alpha, beta, n1, n2);
		k=k-n1;
		alpha = ((alpha-1)/2);
		n1 = 2*n1;
		return odd_splitter(k,alpha, beta, n1, n2);
	}
	else {
		k = k - n1;
		beta = (alpha-1)/2;
		alpha = 0;
		n2 = 2*n1;
		n1 = 0;
		return even_splitter(k,alpha, beta, n1, n2);
}}
void value_updater(long& k,long& alpha, long& beta,long& n1, long& n2){
	if (k>n1+n2) {
		k-=(n1+n2);
		long a = (beta - 1)/2;
		long b = beta/2;
		if ((alpha/2)%2) {
			n1= n1+n1+n2;
			n2 = n2;
		}
		else {
			long temp = n1;
			n1 = n2;
			n2 = temp+temp+n2;
		}
		if (a%2) {
			alpha = a;
			beta = b;
		}
		else {
			alpha = b;
			beta = a;
		}
		return value_updater(k, alpha, beta , n1, n2);
	}
	else return if_found(k, alpha, beta, n1, n2);
	return;
}

void if_found(long & k, long & alpha, long & beta, long & n1, long & n2){
	long a;
	long b;
	long c;
	if (alpha<beta){
		a=n2;
		b=beta;
		c=alpha;
	}
	else {
		a=n1;
		b=alpha;
		c=beta;
	}
	if (k<=a){
		alpha = (b-1)/2;
		beta = b/2;
	}
	else {
		alpha = (c-1)/2;
		beta = c/2;
	}
	return;
}
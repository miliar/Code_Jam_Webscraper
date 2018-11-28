#include<iostream>
#include<fstream>
using namespace std;
int a[200];
int b[200];
int head,total;
void store(int num){
	int i;
	for (i=head;i<total;i++){
		if (a[i]==num) {
			b[i]++;
			return;
		}
	}
	a[total]=num;
	b[total]=1;
	total++;
}
int main(){
	ifstream in("Q3.in");
	ofstream out("Q3.out");
	int n,i,j,k,l,ttt,min,max,x;
	//int a[10010];
	in>>ttt;
	for (i=1;i<=ttt;i++){
		in>>n;
		in>>k;
		out<<"Case #"<<i<<": ";
		for (j=0;j<200;j++) {
			a[j]=0;
			b[j]=0;
		}
		a[0]=n;
		b[0]=1;
		head=0;
		total=1;
		for (j=1;j<=k;j++){
			x=a[head];
			b[head]--;
			if (b[head]==0) head++;
			if (x%2==0){
				max=x/2;
				min=x/2-1;
				store(max);
				store(min);
				//a[max]++;
				//a[min]++;
				//a[x]--;
			} else {
				max=x/2;
				min=x/2;
				store(max);
				store(min);
				//a[max]++;
				//a[min]++;
				//a[x]--;
			}
		} 
		out<<max<<" "<<min<<endl;
	}
}

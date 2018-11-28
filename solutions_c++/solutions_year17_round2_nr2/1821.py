#include<iostream>
using namespace std;

int a[6],n;

int lneighbour(int q){
	if( q == 0)	return 5;
	else return q - 1;
}
	
int rneighbour(int q){	
	if(q == 5)	return 0;
	else return q + 1;
}
	
int valid(int q){
	int left = lneighbour(q), right = rneighbour(q);
	int sum = 0;
	for(int i=0; i < 6; i++){
		if(i == q || i == left || i == right)
				continue;
		sum += a[i];
	}
	if(sum >= a[q]){return true;}
	else {return false;}
}
/*
bool nonzero(){
	for(int i=0; i < 6;i++){
		if(a[i] > 0)
			return true;
	}
	return false;
}*/

void output(int i){
	switch(i){
		case 0: cout<<'R';
				break;
		case 1: cout<<'O';
				break;
		case 2: cout<<'Y';
				break;
		case 3: cout<<'G';
				break;
		case 4: cout<<'B';
				break;
		case 5: cout<<'V';
				break;
		default : cout<<"fail";
				break;
	}
}

int diff(int q){
	int l=lneighbour(q), r=rneighbour(q);
	int sum = 0;
	for(int i=0; i < 6; i++){
		if(i == q || i == l || i == r)
				continue;
		sum += a[i];
	}
	return sum - a[q];
}
	
void print_cycle(int i){
	output(i);
	a[i]--;
	n--;
	int j=rneighbour(rneighbour(i));
	while(j != i && n>0){
		if(a[j]>0){
			output(j);
			a[j]--;
			n--;
		}
		j= rneighbour(rneighbour(j));
	}
}

void print_0_diff(int i){
	int r=rneighbour(rneighbour(i));
	int l=lneighbour(lneighbour(i));
	while(a[i]>0){
		if(a[r] > 0){
			output(i);
			output(r);
			a[i]--;
			a[r]--;
			n-=2;
		}
		else{
			output(i);
			output(l);
			a[i]--;
			a[l]--;
			n-=2;
		}
	}
}
	
void generate(){
	if(n == 0)	return;
	int iter = 0;
	while(a[iter] == 0)
		iter = rneighbour(iter);
	for(int j =iter; j < 6; j++){
		if(a[j] > 0 && diff(iter) > diff(j))
			iter = j;
	}
	while(diff(iter) > 0)
		print_cycle(iter);
	print_0_diff(iter);
	generate();
}

int main(){
	int t;
	cin>>t;
	for(int i=1; i<= t; i++){
		cin>>n>>a[0]>>a[1]>>a[2]>>a[3]>>a[4]>>a[5];
		bool check= true;
		if(n == 0){
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		if(n == 1){
			int iter = 0;
			while(a[iter] == 0)
				iter = rneighbour(iter);
			output(iter);
			continue;
		}
		for(int j=0; j<6 ; j++)
			check = (check & valid(j));
		//cout<<check;
		cout<<"Case #"<<i<<": ";
		if(check == false){
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		generate();
		cout<<endl;
	}
	return 0;
}
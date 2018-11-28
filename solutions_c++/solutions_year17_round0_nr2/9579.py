#include <iostream>
#include<algorithm>
#include <fstream>
#include<sstream>
using namespace std;
int a[20];
bool check(int n){
    for(int i=0;i<n-1;i++){
        if(a[i]>a[i+1]){
            return false;
        }
    }
    return true;
}
int main() {
    ifstream fin("B-large.in");
    ofstream fout("small_input.txt");
    string line;
    getline(fin,line);
    std::istringstream iss(line);
    int t;
    iss>>t;
   // cout<<t<<endl;
    for(int test=0;test<t;test++){
    getline(fin,line);
	std::istringstream is(line);	
	long long int n;
	is>>n;
	long long int j = n;
	int num=0;
	while(j>0){
	    j = j/10;
	    num++;
	}
	j = n;
	int i = 0;
	while(j>0){
	    a[num-1-i] = j%10;
	    j = j/10;
	    i++;
	}
	int number = num;
    while(!check(num)&& num>1){
        if(a[num-2] >a[num-1])
		a[num-2]  = a[num-2]-1;
		else
		a[num-2] = a[num-2]-1;
        a[num-1] = 9;
        num--;
    }
    fout<<"Case #"<<test+1<<": ";
    for(int i=0;i<number;i++){
       if ((i!=0) || (a[i]!=0)){
	    fout<<a[i];
    //   cout<<a[i];}
    }
}
    if(test!= t-1){
    	fout<<endl;
    //	cout<<endl;}
}
}
	return 0;
}


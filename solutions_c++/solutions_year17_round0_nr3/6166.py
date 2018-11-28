#include <iostream>
#include <cmath>
#include <fstream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	long n,k,no,left,right,popped,len,temp;
    ifstream in;
	in.open("C-small-2-attempt1.in");
	ofstream out;
	out.open("output.out");
    std::priority_queue<long> q;
	size_t t;
	in>>t;



	for(size_t test=1;test<=t;test++){

	    in>>n>>k;
	    no=n;
	    q.push(no);
	    while(k){
	    len = q.size();
	    while((len--)&&k){
            temp = q.top();
            q.pop();k--;
            if(temp%2==0){
                q.push(temp/2);
                left=temp/2;right=temp/2-1;
                q.push(temp/2-1);
            }
            else{
                q.push(temp/2);
                left=temp/2;right=temp/2;
                q.push(temp/2);
            }
	    }
        if(right==-1) right++;
        if(k==0) out<<"Case #"<<test<<": "<<left<<" "<<right<<endl;

	    }


    while(q.size()){q.pop();}
    }


	return 0;
}

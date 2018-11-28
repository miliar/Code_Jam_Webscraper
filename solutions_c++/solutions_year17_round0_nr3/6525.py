#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<climits>

using namespace std;

void findStall(vector<bool>& empty,long long k,pair<long long,long long>& p) {
    
    long long i=0,j,left,right;
    long long maxi=LLONG_MIN;
    //1. find the longest empty position
    while(i<empty.size()) {
        if(empty[i]) {
            j=i;
            while(++j<empty.size() && empty[j]);
            if(j-i>maxi) {
                maxi=j-i;
                left=i;
                right=j-1;
            }
            i=j+1;
        }
        else ++i;
    }
    //2. find the position for the current person
    if(maxi%2==0) empty[left+maxi/2-1]=0;
    else empty[left+maxi/2]=0;
    //3. if this is not the last person, continue
    if(k==1) {
        if(maxi%2==0) p=make_pair(maxi/2,maxi/2-1);
        else p=make_pair(maxi/2,maxi/2);
        return;
    }
    else findStall(empty,k-1,p);
}

int main() {
    
    ifstream infile;
    ofstream outfile;
    infile.open("Cs.txt");
    outfile.open("out.txt");
    if(infile.is_open()) {
        int T; //# of cases
        long long n,k;
        pair<long long, long long> p;
        infile>>T;
        for(int i=0;i<T;++i) {
        infile>>n>>k;
        vector<bool> empty(n,1); //initial all empty
        findStall(empty,k,p);
        outfile<<"Case #"<<i+1<<": "<<p.first<<" "<<p.second<<endl;
        }
    }
    infile.close();
    outfile.close();
    /*
    
    int T; //# of cases
    int n,k;
    pair<long long, long long> p;
    cin>>T;
    for(int i=0;i<T;++i) {
        cin>>n>>k;
        vector<bool> empty(n,1); //initial all empty
        findStall(empty,k,p);
        cout<<"Case #"<<i+1<<": "<<p.first<<" "<<p.second<<endl;
    }
    */
    return 0;
}

#include <iostream>
#include <fstream>

using namespace std;

int main()
{

    long t,arr[50],len;
    string n;
    ifstream infile;
    ofstream outfile;
    outfile.open("B-small-attempt0.out");
    infile.open("B-large.in");
    infile>>t;
    int k=1;
    while(k<=t){
        infile>>n;
        len = n.length();
        long pt=len-1;long start = 0;
        for(long i=0;i<len;i++){
            arr[i] = int(n[i]-'0');
        }
    while(pt>0){
    if(arr[pt]<arr[pt-1]){
        if(pt-1!=0){
            arr[pt-1]--;
            for(int i=pt;i<len;i++){
                arr[i]=9;
            }
        }
        else if(pt-1==0&&arr[pt-1]==1){
            arr[pt]=9;
            start++;
            for(int i=start+1;i<len;i++){
                arr[i]=9;
            }
        }
        else if(pt-1==0){
            arr[pt-1]--;
            for(int i=start+1;i<len;i++){
                arr[i]=9;
            }
        }
    }
    pt--;
    }

    outfile<<"Case #"<<k<<": ";
    for(int i=start;i<len;i++){
        outfile<<arr[i];
    }
    outfile<<endl;
    k++;


    }

    return 0;
}

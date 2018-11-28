#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream file;
    file.open("output.txt");
    int t;
    cin>>t;

    for(int i=1;i<=t;i++){
            int n,k;
            cin>>n>>k;

            vector<int> index;
            int globalIndex;
            index.push_back(0);
            index.push_back(n+1);
            int number = 1;
            while(number <= k ){
                sort(index.begin(),index.end());
                int maxi=1;
                int maxiIndex=-1;
                for(int p=0;p<index.size()-1;p++){
                    if(maxi < (index[p+1]-index[p])){
                        maxi = (index[p+1]-index[p]);
                        maxiIndex = p;
                    }
                }
                int newIndex = index[maxiIndex]+((index[maxiIndex+1]-index[maxiIndex])/2);

                if(number==k){
                        globalIndex = newIndex;
                }
                index.push_back(newIndex);
                number++;
            }
            sort(index.begin(),index.end());
           
            int maxAns,minAns;
            for(int p=1;p<index.size()-1;p++){
                if(index[p]==globalIndex){
                    maxAns = index[p]-index[p-1] > index[p+1]-index[p] ? index[p]-index[p-1] : index[p+1]-index[p];
                    minAns = index[p]-index[p-1] < index[p+1]-index[p] ? index[p]-index[p-1] : index[p+1]-index[p];
                }
            }
        string x3 = "Case #";

        stringstream ss2;
        ss2<<i;
        string y;
        ss2>>y;

        string x4 = ": ";

        stringstream ss3;
        ss3<<maxAns-1;
        string s3;
        ss3>>s3;

        stringstream ss4;
        ss4<<minAns-1;
        string s4;
        ss4>>s4;

        string y2 = s3+" "+s4;


        string x;
        x = x3+y+x4+y2+"\n";
        file<<x;

            


    }

    return 0;
}

#include <iostream>
#include <string>
using namespace std;

int totalFlip(string pancakes, int cakeSize, long flipSize){
    //cout<<pancakes.find('-')<<endl;
    int loop = 0;
    int pcLen = (int)pancakes.length();
    while(pancakes.find('-') != -1){
        int loc = pancakes.find("-");
        if(pcLen-(loc+flipSize) >=0){
            for(int j=1;j<=flipSize;j++,loc++){
                if(pancakes[loc] =='+'){
                    pancakes[loc]='-';
                } else {
                    pancakes[loc]='+';
                }
            }
        }
        //cout<<pancakes<<endl;
        loop++;
        if(loop > cakeSize){
            loop = -1;
            break;
        }
    }

    return loop;
}


int main(){
    //reading file
    int t,n,m;
    cin >> t;
    //Ignore the Integer at input 
    string line;
    getline(cin, line);

    for(int i = 1; i<=t; i++){
        getline(cin, line);
        string pc = line.substr(0,line.find(" "));
        string fsStr = line.substr(line.find(" ")+1);
        char *fsPtr = new char[fsStr.length()+1];
        strcpy(fsPtr,fsStr.c_str());
        long fs = strtol(fsPtr,NULL,10);

        int result = totalFlip(pc,pc.length(),fs);
        if(result == -1){
            cout << "Case #" <<i<<": "<<"IMPOSSIBLE"<<endl;
        } else {
            cout << "Case #" <<i<<": "<<result<<endl;
        }
        
    }

    return 0;
}
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int getNumCases(string fileName){
    string line;
    ifstream myfile (fileName);
    if (myfile.is_open()){
        getline (myfile,line);
    }
    else cout << "Unable to open file";

    int cases=stoi(line);
    return cases;
}

int readCase(string fileName, int i){
    string line;
    ifstream myfile (fileName);
    if (myfile.is_open()){
        for (int lineno = 0; getline (myfile,line) && lineno < i; lineno++)
              if (lineno == i)
                  cout << line<< '\n';
    }
    else
        cout << "Unable to open file";

    int caseNum=stoi(line);
    return caseNum;

}

int numDigits (int num) {
   int count =0;
   while (num !=0) {
      count++;
      num/=10;
   }
   return count;
}

bool compareLast2Digits(int n){
    int end=0;
    int beforeEnd=0;
    int leftOver=0;
    end=n%10;
    leftOver=n/10;
    beforeEnd=leftOver%10;
    if(end>=beforeEnd){
        return true;
    }
    return false;
}

bool isTidyNumber(int num){
    int digits=numDigits(num);
    int compare=num;
    bool isTidy=true;
    for(int i=0;i<digits;i++){
        if(compareLast2Digits(compare)==true){
            compare=compare/10;
        }
        else{
            isTidy=false;
            break;
        }
    }
    return isTidy;
}

int lastTidyNumber(int num){
    int tidynum=num;
    for(int i=num; i>=1; i--){
        if(isTidyNumber(i)==true){
            tidynum=i;
            break;
        }
    }
    return tidynum;
}

int main(){
    ofstream outputFile;
    outputFile.open("output.txt");

    for(int i=1; i<=getNumCases("B-small-attempt1.in"); i++){
        int test=readCase("B-small-attempt1.in",i);
        int ans=lastTidyNumber(test);
        //cout<<"case # "<<i<<'\t'<<" : "<<ans<<'\n';
        outputFile<<"Case #"<<i<<": "<<ans<<'\n';
    }
}

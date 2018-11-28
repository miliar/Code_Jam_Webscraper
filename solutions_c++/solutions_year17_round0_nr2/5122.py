#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>
#include <fstream>

using namespace std;

queue < pair<long long int, int> > a;
vector <long long int> num;


void preproc(){
pair <long long int, int> temp,temp1;
long long temp2,temp3;
for(int i=1;i<=9;i++) {
    temp = make_pair(i,1);
    a.push(temp);
    num.push_back(temp.first);
}


while(a.front().second<18){

    //cout << a.front().second << endl;
    temp=a.front();
    a.pop();
    temp2=temp.first;
    for(int i=temp2%10;i<=9;i++){
        temp3=temp2*10+i;
        temp1=make_pair(temp3,temp.second+1);
        a.push(temp1);
        num.push_back(temp1.first);
    }


}



 return;
}



int main(){
preproc();
ifstream myfile("sample.txt");
ofstream ifile("large.txt");
/*for(long i=0;i<1000;i++)
    myfile << num[i]<<endl;
*/
//cout << num[num.size()-1] << endl;

int t;
myfile >> t;
for(int tt=1;tt<=t;tt++){
    long long n;
    myfile >> n;
    vector<long long>::iterator low;
    low=upper_bound(num.begin(),num.end(),n);

    ifile <<"Case #" << tt << ": " <<*(low-1) << endl;

}



return 0;
}

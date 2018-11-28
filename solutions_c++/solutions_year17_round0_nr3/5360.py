#include<iostream>
#include<queue>

using namespace std;

int main() {
  int T;
  long long int N,K;
  cin>>T;
  queue<long long int> distance; //storing the distances between people
  for (int i=1;i<=T;i++) {
    cin>>N>>K;
    distance.push(N);
    long long int count=1;
    long long int temp, large, small, j=1;
    while (j<=K) {
      temp=distance.front();
      distance.pop();
      count=1;
      while (temp==distance.front()&&j<K) { //counting all the same distance between people
        distance.pop();
        count++;
        j++;
      }
      if (temp%2==0) {
        for (long long int k=1;k<=count;k++) distance.push(temp/2);
        for (long long int k=1;k<=count;k++) distance.push(temp/2-1);
      }
      else {
        for (long long int k=1;k<=2*count;k++) distance.push(temp/2);
      }
      j++;
    }
    if (temp%2==0) {large=temp/2; small=temp/2-1;}
    else {large=temp/2; small=temp/2;}
    cout<<"Case #"<<i<<": "<<large<<" "<<small<<endl;
    while (!distance.empty()) distance.pop();
  }
  return 0;
}

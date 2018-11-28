#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<fstream>
#include<string>
#include<list>
#include<stack>
#include<unordered_set>

using namespace std;

/*
Author: Utkarsh Verma
Email ID: utkarsh13103453cse@gmail.com
Contact: +91 9871271616

*/

long long base(int power){
long long ret=1;
while(power>0){
ret*=10;
power--;
}

return ret;
}


int tidy(long long K){
    string sorted,unsorted,number=to_string(K);
//    cout<<"tidy called for: "<<K<<endl;
    if(K==K%10){
        return -1;
    }else{
        for(int i=1;i<=number.length();i++){
            unsorted=to_string(K%base(i));
            sorted=unsorted;
            sort(sorted.begin(),sorted.end());
//            cout<<endl<<"sorted: "<<sorted<<endl;
            if(sorted!=unsorted){
            return i;
            }
        }
        return 0;
    }
}

long long func(long long K){

    int tidy_int=tidy(K);
//    cout<<"tidy returned: "<<tidy_int<<endl;
    while(tidy_int>0){
//        cout<<K<<endl;
        K-=((K%base(tidy_int-1))+1);

//        cout<<" k agter - "<<((K%base(tidy_int-1)))<<endl;
        tidy_int=tidy(K);
//    cout<<"tidy returned: "<<tidy_int<<endl;

    }
    return K;

}

//int main(){
//    long long n;
//    cin>>n;
//
//    cout<<func(n)<<endl;
//
//    main();
//}

int main()
{
  ifstream infile;
  ofstream outfile;
  infile.open ("small_input_tidy.txt");
  outfile.open("small_output_tidy.txt");
  int N;
  infile>>N;
  for(int i=1;i<=N;i++)
  {
    long long K;
    infile>>K;

    outfile<<"Case #"<<i<<": "<<func(K)<<endl;
  }

  //cout<<s;
  //outfile<<s;
  infile.close();
  outfile.close();
return 0;
}

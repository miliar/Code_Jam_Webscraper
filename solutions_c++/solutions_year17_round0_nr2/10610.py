#include <iostream>
//#include <fstream>
#include <string>

using namespace std;
bool isTidy ( std::string s );
void replaceTidy( uint64_t &tidy,std::string s);

int   main()
{
	/*ifstream in("/home/shimaa/Desktop/contest/A-small-attempt1.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("/home/shimaa/Desktop/contest/A-small-attempt1.out");
	cout.rdbuf(out.rdbuf());*/
    int t ;
    uint64_t n;
    uint64_t tidy;
    std::string s;
    cin >>t ;
    for (int i = 0 ; i < t ; i ++){
        cin >> n;
        if (n<10){cout << "Case #"<<i+1<<": "<<n<<endl;}
        else {
            for (uint64_t j = n ; j > 0; j--){
            s=std::to_string(j);
            if (isTidy(s)){replaceTidy(tidy,s);break;}
            }
            cout << "Case #"<<i+1<<": "<<tidy<<endl;}
        }

}

bool isTidy ( std::string s ){
    uint64_t size=s.length()-1;
    int p,n;
    string s1,s2;
    for (uint64_t i = 0 ; i < size;i++){
        s1=s[i];s2=s[i+1];
        p=stoi(s1);
        n=stoi(s2);
        if (p>n)return false;
        }
    return true;
    }
void replaceTidy( uint64_t &tidy,std::string s){
    uint64_t nt=stoll(s);
    tidy = nt;
    }

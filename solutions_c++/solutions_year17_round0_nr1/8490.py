#include <iostream>
#include <string>
#include <bitset>         // std::bitset
#include <queue>
#include <set>
#include <algorithm> // std::queue
using namespace std;


int number;
vector < vector<string> > root;


string Flipit(string con,int pos,int l)
{

    for(int i=pos;i<l+pos;i++)
        if(con[i]=='+')
            con[i]='-';
    else if(con[i]=='-')
        con[i]='+';

    return con;
}

bool Check(vector < vector<string> > rt,string con)
{
    for(auto x : rt)
        for(auto xx : x)
           {
                if(xx==con) return false;
           }
    return true;
}

string Minimumuses(vector < vector<string> > cc,int n)
{

    vector<string> tleaves,result;
    set <string> leaves;

    auto conf = cc.back();

    for(auto config : conf)
    {
        for(int i=0;i<=config.size()-n;i++)
        {

            if (!std::any_of(config.begin(), config.end(), [](char i){ return i=='-'; }))
            {

                return to_string(root.size()-1);
            }


            string a;
            a = Flipit(config,i,n);



            if(Check(cc,a))
            leaves.insert(a);

        }
    }

    if(leaves.empty()) return "IMPOSSIBLE";

    for(auto lv : leaves)
    {
        tleaves.push_back(lv);
  //      cout << lv << "\n";
    }
//    cout << "\n";


     root.push_back(tleaves);

     return Minimumuses(root,n);








//    for(auto l:result)
//        cout << l << "\n";

    //return config;



}


int main(int argc, char *argv[])
{

    int tc; cin >> tc;
    vector<string> temp;

    for(int i=1;i<=tc;i++)
    {
        string config;

        cin >> config >> number;

        temp.push_back(config);
        root.push_back(temp);

        cout << "Case #"<<i<<": "<< Minimumuses(root,number)<<"\n";

        temp.clear();
        root.clear();
    }

    return 0;
}

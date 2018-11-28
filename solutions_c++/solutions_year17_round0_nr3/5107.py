#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("bathroom2.in", ios::in);
    fout.open("output.txt", ios::out);

    int t;
    fin>>t;
    int casecount = 0;
    while(t--)
    {
        casecount++;
        cout<<casecount<<endl;
        long long int n, k, ls, rs;
        priority_queue<long long int> q;
        fin>>n>>k;

        q.push(n);
        while(k--)
        {
            n = q.top();
            q.pop();

            if(n <= 0)
                break;

            if(n&1)
            {
                ls = rs = n/2;
            }
            else
            {
                ls = n/2-1;
                rs = n/2;
            }

            q.push(rs);
            q.push(ls);

        }
        fout<<"Case #"<<casecount<<": "<<rs<<" "<<ls<<endl;
    }
}

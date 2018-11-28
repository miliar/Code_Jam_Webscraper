#include<functional>
#include<queue>
#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

void val(int &a, int &b)
{
    if(a%2 == 1)
    {
        a /= 2;
        b = a;
        return;
    }

    a /= 2;
    b = a-1;

}

void clear( priority_queue<int> &q )
{
   priority_queue<int> empty;
   swap( q, empty );
}

int main()
{
    ifstream fin;
    fin.open("in.in");

    ofstream fout;
    fout.open("out.txt");

    priority_queue<int> q;

    int n, k, t, i=0;

    fin>>t;

    while( i<t && ++i)
    {
        fin>>n>>k;
        q.push(n);

        int a, b = 0;

        while(k--)
        {
            //cout<<q.top()<<endl;
            a = q.top();
            q.pop();
            val(a, b);

            //cout<<a<<" "<<b<<endl;

            q.push(a);
            q.push(b);
        }

        fout<<"Case #"<<i<<": "<<a<<" "<<b<<endl;

        clear(q);
    }
}

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define MP make_pair

int main()
{
    ofstream file;
    file.open("output.txt");
    ifstream infile;
    infile.open("C-small-2-attempt4.in");

    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int T;
    unsigned long long int N, K, temp, temp1, y, z;

    infile >> T;

    for(int lel = 1; lel <= T; ++lel)
    {
        infile >> N >> K;
        priority_queue <long long int> myq;
        myq.push(N);
        while(true)
        {
            temp = myq.top();
            if(K == 1)
            {
                if(temp %2 == 1)
                {
                    y = z = (temp-1)/2;
                }
                else
                {
                    y = temp/2;
                    z = (temp-1)/2;
                }
                break;
            }
            myq.pop();
            --K;
            if(temp == 1)
            {
                continue;
            }
            else if(temp ==2)
            {
                myq.push(1);
            }
            else
            {
                if(temp % 2 == 0)
                {
                    myq.push(temp/2);
                    myq.push((temp-1)/2);
                }
                else
                {
                    temp1 = (temp-1)/2;
                    myq.push(temp1);
                    myq.push(temp1);
                }
            }
        }

        file << "Case #"<< lel+50 <<": "<< y << " "<< z<<"\n";
    }
    return 0;
}

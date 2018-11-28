#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;
/*problema: per cagare in pace devi trovare un cesso che sia abbastanza isolato*/
int main(int argc, char** argv)
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("C-small-2-attempt0.out","w",stdout);
    ULLI n;
	cin >> n;
	for(ULLI i=0; i<n; i++)
    {
        ULLI stalls, people, res1, res2, elem, half;
        cin >> stalls >> people;
        priority_queue<ULLI> frees;

        if(stalls == people)
            res1 = res2 = 0;
        else
        {
            frees.push(stalls);
            for(ULLI j=0; j<people; j++)
            {
                elem = frees.top();
                half = round(elem/2);
                if(half>0 || j==people-1)
                {
                    if(!(elem%2))
                    {
                        frees.push(half);
                        if(half-1>0)
                            frees.push(half-1);
                    }
                    else
                    {
                            frees.push(half);
                            frees.push(half);
                    }
                    res1 = half;
                    res2 = (elem%2)==0? half-1 : half;
                }
                frees.pop();
                /*cerr << "person " << j+1 << endl;
                priority_queue<ULLI> tmp = frees;
                while(!tmp.empty())
                {
                    cerr << tmp.top() << " ";
                    tmp.pop();
                }
                cerr << endl;*/
            }
        }
        cout << "Case #" << i+1 << ": " << res1 << " " << res2 << endl;
        /*ULLI val = stalls/people;
        cout << "Case #" << i+1 << ": " <<  val/2 << " ";
        if(val%2 == 0 && val/2>0)
            cout << val/2 - 1;
        else
            cout << val/2;
        cout << endl;*/
    }
    return 0;
}

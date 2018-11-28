#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct set
{
    long long int num;
    long long int freq;
};

int main()
{
    int T;
    cin >> T;


    for(int t = 0; t < T; t++)
    {
        long long int N;
        long long int K;
        vector<set> appear;
        cin >> N;
        cin >> K;

        set first;
        first.num = N;
        first.freq = 1;
        appear.push_back(first);

//        unsigned long long int temp = N;
        long long int max_;
        long long int min_;


        int count = 0;
        while(1)
        {
            count ++;
            if(count > 100)
                break;
//            for(size_t c = 0; c < appear.size(); c++)
//                cout << appear[c].num << " ";
//            cout << endl;
//            cout << "K: "<< K<< endl;
            K-=appear[0].freq;
//            cout << appear[0].num <<", "<<appear[0].freq<<endl;
            if(K<=0)
                break;
            else
            {
                if((appear[0].num)%2 == 1)
                {
                    long long int new_f = appear[0].freq*2;
                    set new_in;
                    new_in.num = (appear[0].num)/2;
                    new_in.freq = new_f;
                    for(size_t i = 0; i < appear.size(); i++)
                    {
                        if(appear[i].num >new_in.num && i!=appear.size()-1)
                            continue;
                        else if(appear[i].num >new_in.num && i==appear.size()-1)
                        {
                            appear.push_back(new_in);
                            break;
                        }
                        else if(appear[i].num == new_in.num)
                        {
                            appear[i].freq += new_in.freq;
                            break;
                        }
                        else
                        {
                            vector<set>::iterator it = appear.begin();
                            appear.insert(it+i,new_in);
                            break;
                        }
                    }
                    appear.erase(appear.begin());
                }
                else
                {
                    long long int new_f = appear[0].freq;
                    set new_in1;
                    set new_in2;
                    new_in1.num = (appear[0].num/2);
                    new_in1.freq = new_f;
                    new_in2.num = (appear[0].num/2)-1;
                    new_in2.freq = new_f;
                    
                    for(size_t i = 0; i < appear.size(); i++)
                    {
                        if(appear[i].num >new_in1.num && i!=appear.size()-1)
                            continue;
                        else if(appear[i].num >new_in1.num && i==appear.size()-1)
                        {
                            appear.push_back(new_in1);
                            break;
                        }
                        else if(appear[i].num == new_in1.num)
                        {
                            appear[i].freq += new_in1.freq;
                            break;
                        }
                        else
                        {
                            vector<set>::iterator it = appear.begin();
                            appear.insert(it+i,new_in1);
                            break;
                        }
                    }
                    for(size_t i = 0; i < appear.size(); i++)
                    {
                        if(appear[i].num >new_in2.num && i!=appear.size()-1)
                            continue;
                        else if(appear[i].num >new_in2.num && i==appear.size()-1)
                        {
                            appear.push_back(new_in2);
                            break;
                        }
                        else if(appear[i].num == new_in2.num)
                        {
                            appear[i].freq += new_in2.freq;
                            break;
                        }
                        else
                        {
                            vector<set>::iterator it = appear.begin();
                            appear.insert(it+i,new_in2);
                            break;
                        }
                    }
                    appear.erase(appear.begin());
                }
            }
        }
        if((appear[0].num)%2 == 1)
        {
            max_ = (appear[0].num/2);
            min_ = (appear[0].num/2);
        }
        else
        {
            max_ = (appear[0].num/2);
            min_ = (appear[0].num/2)-1;
        }
        cout << "Case #"<<t+1<<": "<<max_<<" "<<min_<<endl;
    }
    return 0;
}


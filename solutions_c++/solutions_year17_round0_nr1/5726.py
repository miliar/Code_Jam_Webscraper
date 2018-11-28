#include <iostream>
#include <map>
#include <cstring>
#include <queue>
#include <set>
#include <fstream>


class cmp{
public:
    bool operator()(std::pair<std::string,u_int*> & a,std::pair<std::string,u_int*> &b)
    {
        return *(a.second)>*(b.second);
    }
};

int iteration(std::string & status,u_int K)
{
    std::string start=status;
    //std::cout<<start<<std::endl;
    for(u_int i=0;i<status.length();i++)
    {
        status[i]=~char(0);
    }

    std::priority_queue<std::pair<std::string,u_int * >,std::vector<std::pair<std::string,u_int *>>,cmp> Q;
    std::map<std::string,bool> C;
    std::map<std::string,u_int> ANS;
    ANS[start]=0;
    Q.push(std::make_pair(start,&ANS[start]));
    ANS[start]=0;


    while(!Q.empty())
    {
        auto temp=Q.top();
        Q.pop();
        C[temp.first]=true;
        start=temp.first;
        if(start==status)
            break;


        for(u_int i=0;i<=start.length()-K;i++)
        {
            std::string starttemp=start;
            for(u_int j=i;j<K+i;j++)
            {
                starttemp[j]=~starttemp[j];
            }
          //  std::cout<<starttemp<<std::endl;

            if(ANS.find(starttemp)==ANS.end())
                ANS[starttemp]=ANS[start]+1;
            if(ANS[starttemp]>ANS[start]+1)
                ANS[starttemp]=ANS[start]+1;
            if(C.find(starttemp)==C.end())
                Q.push(std::make_pair(starttemp,&ANS[starttemp]));

        }

    }

    if(ANS.find(status)==ANS.end())
        return -1;
    else
        return ANS[status];


}




int main(int argc,char **argv) {


    std::ifstream in(argv[1]);
    std::ofstream out(argv[2]);


    int linenum=0;
    in>>linenum;

    std::string currentstr;
    u_int K;


    for(int i=0;i<linenum;i++)
    {
        in>>currentstr>>K;

        for (int i = 0; i < currentstr.length(); i++) {
            if (currentstr[i] == '+')
                currentstr[i] = ~char(0);
            else
                currentstr[i] = char(0);
        }

        int ans=iteration(currentstr,K);
        if(ans!=-1)
            out<<"Case #"<<i+1<<": "<<ans<<std::endl;
        else
            out<<"Case #"<<i+1<<": IMPOSSIBLE"<<std::endl;
    }


    return 0;

}


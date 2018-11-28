#include<iostream>
#include<vector>

using namespace std;
struct stall
{
    int l;
    int r;
    bool occupied;
    struct stall *next;
    struct stall *prev;
};

int main()
{
    int T;
    cin >> T;
    int round=1;
    while(T-- > 0)
    {
        int N, K;
        cin >> N >> K;
        struct stall *head, *previous, *tail;
        struct stall *selected;
        for(int i=0; i<N+2; i++)
        {
            struct stall *node = (struct stall*) new(struct stall);
            if(i==0)
            {
                node->occupied=true;
                node->prev = NULL;
                node->next = NULL;
                node->l=-1;
                node->r=-1;
                head = node;
                previous = node;
            }

            else if(i==N+1)
            {
                node->occupied=true;
                previous->next = node;
                node->prev = previous;
                node->next = NULL;
                node->l=-1;
                node->r=-1;
                tail = node;

            }
            else
            {
                node->occupied=false;
                previous->next = node;
                node->prev = previous;
                node->next = NULL;
                node->l=i-1;
                node->r=N-1;
                previous = node;
            }
        }
        for(int j=1; j<=K; j++)
        {
            struct stall *p = head->next;

            int overallmin = -1;
            while(p!=tail)
            {
                if(!p->occupied)
                {
                    struct stall *left=p;
                    int cnt=0;
                    while(left->prev!=NULL)
                    {
                        left = left->prev;
                        if(!left->occupied)
                            cnt++;
                        else
                            break;
                    }
                    p->l = cnt;

                    cnt=0;
                    struct stall *right = p;
                    while(right->next != NULL)
                    {

                        right = right->next;
                        if(!right->occupied)
                            cnt++;
                        else
                            break;
                    }
                    p->r = cnt;

                    int minimum = min(p->l,p->r);


                    if(minimum > overallmin)
                    {
                        overallmin = minimum;
                        selected = p;
                    }
                    else if(minimum == overallmin)
                    {
                        int maximum1 =max(p->l, p->r);
                        int maximum2 = max(selected->l, selected->r);
                        if(maximum1 > maximum2)
                        {
                            selected = p;
                        }
                    }
                    //cout<<overallmin;
                }
                p = p->next;

            }
           selected->occupied=true;
        }
        cout << "Case #" << round << ": " << max(selected->l, selected->r) << " " << min(selected->l, selected->r) << "\n";
        round++;
    }

    return 0;
}

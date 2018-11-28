#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <map>
#include <cstddef>
#include <cstddef>

using namespace std;

struct node
{
    int info;
    struct node *next;
    struct node *prev;
};

class Queue
{
private:
    node *rear;
    node *front;
public:
    Queue();
    void enqueue(int);
    int dequeue();
    void display();
};

Queue::Queue()
{
    rear = NULL;
    front = NULL;
}

void Queue::enqueue(int data)
{
    node *temp = new node;
    temp->info = data;
    temp->next = NULL;
    temp->prev = NULL;
    if(front == NULL)
    {
        front = temp;
        rear = temp;
    }
    else if(rear->info >= data)
    {
        temp->prev = rear;
        rear->next = temp;
        rear = temp;
    }
    else
    {
        temp->next=rear;
        temp->prev=rear->prev;
        while(temp->prev->info<data)
        {
            temp->next=temp->prev;
            temp->prev=temp->next->prev;
        }
        temp->next->prev = temp;
        temp->prev->next =temp;
    }
}

int Queue::dequeue()
{
    node *temp = new node;
    int hold;
    if(front == NULL)
    {
        delete temp;
        return -1;
    }
    else if (front == rear)
    {
        temp = front;
        hold = temp->info;
        delete temp;
        rear = NULL;
        front = NULL;
        return hold;
    }
    else
    {
        temp = front;
        front = front->next;
        front->prev = NULL;
        hold = temp->info;
        delete temp;
        return hold;
    }
}

void Queue::display()
{
    node *p = new node;
    p = front;
    if(front == NULL)
    {
        cout<<"\nNothing to Display\n";
    }
    else
    {
        while(p!=NULL)
        {
            cout<<endl<<p->info;
            p = p->next;
        }
    }
}

int main()
{
    char a[100];
    int no_of_elem = 0;
    int stl = 0;
    int ppl = 0;
    int data;
    int l,r;
    ofstream outfile;
    outfile.open("out.txt");
    ifstream infile;
    infile.open("C-small-1-attempt4.in");
    Queue q;

    infile >> a;
    no_of_elem = atoi(a);


    for (int i = 0; i < no_of_elem; ++i)
    {
        infile >> a;
        stl = atoi(a);
        infile >> a;
        ppl = atoi(a);

        data = stl;
        for(int j = 0; j< ppl-1; ++j)
        {
            if(data==0)
            {
                data = q.dequeue();//outfile<< "Invalid dequeue again" <<endl;
            }
            else if(data==1)
            {
                //outfile<< "no of ppl: " << j << "at" << 1 << " no data queued" << endl;
            }
            else if(data == 2)
            {
                q.enqueue(1);//outfile<< "no of ppl: " << j << " at " << 0 << " data queued 1"<<endl;
            }
            else if(data%2 == 0)
            {
                q.enqueue(data/2);
                q.enqueue((data/2)-1);//outfile<< "no of ppl: " << j << " at " << data << " data queued " << data/2 <<" "<< (data/2)-1 <<endl;
            }
            else
            {
                q.enqueue(data/2);//outfile<< "no of ppl: " << j << " at " << data << " data queued " << data/2 <<" "<< (data/2) <<endl;
                q.enqueue(data/2);
            }
            data = q.dequeue();
        }
        if(data==1)
        {
            outfile << "Case #" << i+1 << ": " << 0 << " " << 0 << endl;
        }
        else if(data%2 == 0)
        {
            l = (data/2)-1;
            r = (data/2);
            outfile << "Case #" << i+1 << ": " << max(l,r) << " " << min(l,r) << endl;
        }
        else
        {
            l = (data/2);
            r = (data/2);
            outfile << "Case #" << i+1 << ": " << max(l,r) << " " << min(l,r) << endl;
        }
        q.enqueue(-1);
        while(q.dequeue()!=-1)
        {
            i++;
            i--;
        }
    }

    outfile.close();
    infile.close();

    return 0;
}

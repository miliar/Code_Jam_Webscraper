#include <iostream>

#include <QString>
#include <QFile>
#include <QTextStream>

using namespace std;

//using Qt5.7 libraries

double steed_control(int dst, int N, int *pos, int *speed)
{
    double time = DBL_MIN;
    double *duration = (double*)malloc(sizeof(double) * N);
    int i = 0, j = 0;
    double num, den, x;

    for(i = 0;i < N;i++)
    {
        num = dst - pos[i];
        den = speed[i];
        duration[i] = num / den;
    }

    for(i = 0;i < N-1;i++)
    {
        for(j = 1;j < N;j++)
        {
            num = (speed[j]*pos[i]) - (speed[i]*pos[j]);
            den = (speed[j] - speed[i]);
            x = (num / den);
            if(x > pos[i] && x > pos[j] && x < dst)
            {
                if(speed[i] < speed[j])
                    duration[j] = ((double)(x - pos[j]) / (double)speed[j]) +
                            ((double)(dst - x) / (double)speed[i]);

                if(speed[j] < speed[i])
                    duration[i] = ((double)(x - pos[i]) / (double)speed[i]) +
                            ((double)(dst - x) / (double)speed[j]);
            }
        }
    }

    for(i = 0;i < N;i++)
    {
        if(time < duration[i])
            time = duration[i];
    }

    free(duration);

    return dst / time;
}

QString unicorn_shed(int N, int *types, int pos, char *arrangement)
{
    for(int i = 0;i < 7;i++)
    {
       if(types[i] > 0)
       {

       }
    }
    return QString();
}

int main(int argc, char *argv[])
{
    int cases, D, N, i, j;
    int *pos, *speed;
    QString input, temp;
    QStringList parts;
    QFile file("D:\\Round2\\A-large.in");
    FILE *fp = fopen("D:\\Round2\\A-large-output.txt", "a");

    if(fp && file.open(QIODevice::ReadOnly))
    {
        QTextStream stream(&file);
        while(!stream.atEnd())
        {
            cases = stream.readLine().toInt();
            for(i = 1;i <= cases;i++)
            {
                input = stream.readLine();
                parts = input.split(" ", QString::SkipEmptyParts);
                temp = parts.at(0);
                D = temp.toInt();
                temp = parts.at(1);
                N = temp.toInt();

                pos = (int*)malloc(sizeof(int) * N);
                speed = (int*)malloc(sizeof(int) * N);

                for(j= 0;j < N;j++)
                {
                    input = stream.readLine();
                    parts = input.split(" ", QString::SkipEmptyParts);
                    temp = parts.at(0);
                    pos[j] = temp.toInt();
                    temp = parts.at(1);
                    speed[j] = temp.toInt();
                }

                fprintf(fp, "Case #%d: %.6f\n", i, steed_control(D, N, pos, speed));
                free(pos);
                free(speed);
            }
            fclose(fp);
        }
    }
    file.close();
}

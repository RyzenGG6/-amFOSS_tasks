#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;
    do
    {
        printf("Height:");
        scanf("%d", &h);
    } while (h < 1 || h > 8);
    for (int i = 1; i <= h; i++)
    {
        for (int j = 1; j <= h - i + 1; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= i; j++)
        {
            printf("#");
            if (j == i)
            {
                printf("  ");
            }
        }
        for (int j = i; j >= 1; j--)
        {
            printf("#");
        }

        printf("\n");
    }
}